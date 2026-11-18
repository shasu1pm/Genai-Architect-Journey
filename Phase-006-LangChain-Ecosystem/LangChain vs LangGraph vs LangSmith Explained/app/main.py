"""FastAPI layer — the HTTP interface of the AI Learning Assistant.

GET  /health        application, provider and LangSmith status
POST /ask           LangChain alone: one chain, one model call
POST /workflow      the full LangGraph workflow (classify → explain → example → validate → retry/fallback)
GET  /docs          Swagger UI (generated from the code)
GET  /openapi.json  OpenAPI specification

Run from the project folder:  uvicorn app.main:app --reload
"""
from __future__ import annotations

import logging
import time
import uuid
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, JSONResponse
from langchain_core.exceptions import OutputParserException
from langchain_core.language_models.chat_models import BaseChatModel
from starlette.exceptions import HTTPException as StarletteHTTPException

from app import __version__
from app.chains import answer_question
from app.config import PROJECT_DIR, get_settings, provider_problem, setup_logging
from app.graph import run_workflow
from app.llm import MOCK_NOTE, get_chat_model
from app.observability import configure_tracing, run_config
from app.schemas import AskResponse, ErrorResponse, HealthResponse, QuestionRequest, WorkflowResponse

BRAND = "Shasu Vathanan - GEN AI - Product Manager"
BRAND_DIR = PROJECT_DIR.parents[1] / "zz-Brand-Assets"     # brand images used as they are
BRAND_FILES = {"logo.png": BRAND_DIR / "Dragon-Motivation-Logo.png", "negot.png": BRAND_DIR / "NeGot-My-AI-Avatar.png"}
ERROR_CODES = {400: "bad_request", 404: "not_found", 405: "method_not_allowed", 422: "validation_error",
               502: "model_error", 503: "service_unavailable"}

log = logging.getLogger("learning_assistant")


@asynccontextmanager
async def lifespan(_: FastAPI):
    settings = get_settings()
    setup_logging(settings.log_level)
    tracing = configure_tracing(settings)
    log.info("Starting AI Learning Assistant %s | provider=%s model=%s | LangSmith tracing=%s",
             __version__, settings.llm_provider, settings.model_name, "on" if tracing["enabled"] else "off")
    if problem := provider_problem(settings):
        log.warning(problem)
    yield


app = FastAPI(
    title="AI Learning Assistant | Shasu Vathanan",
    version=__version__,
    description=(
        '<img src="/brand/logo.png" alt="Dragon Motivation logo" height="56"> '
        '<img src="/brand/negot.png" alt="NeGot - my AI avatar" height="52">\n\n'
        f"**{BRAND}**\n\n"
        "Ask an educational question and get a beginner-friendly explanation with a real-world example.\n\n"
        "- **POST /ask** — LangChain alone: prompt template → chat model → structured output.\n"
        "- **POST /workflow** — LangGraph: classify → explain → add example → validate, with a bounded retry and a fallback.\n"
        "- LangSmith tracing is optional and returns a `trace_id` when enabled.\n\n"
        "In **mock mode** every answer is predefined and labelled as such — no model is called.\n\n"
        "[SHASUVATHANAN.COM](https://shasuvathanan.com) · [LinkedIn](https://www.linkedin.com/in/shasuvathanan) · "
        "[GitHub](https://github.com/shasu1pm/Genai-Architect-Journey)"
    ),
    contact={"name": BRAND, "url": "https://shasuvathanan.com"},
    docs_url=None,
    lifespan=lifespan,
)

ERROR_RESPONSES = {
    422: {"model": ErrorResponse, "description": "The question is missing, blank, too short or too long"},
    503: {"model": ErrorResponse, "description": "The configured LLM provider cannot be used (for example, a missing key)"},
}


# ----------------------------------------------------------------------------- logging and errors
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """One log line per request: method, path, status and duration. Bodies and headers are never logged."""
    request_id = uuid.uuid4().hex[:12]
    started = time.perf_counter()
    response = await call_next(request)
    log.info("%s %s -> %s in %.0f ms [request %s]", request.method, request.url.path, response.status_code,
             (time.perf_counter() - started) * 1000, request_id)
    response.headers["X-Request-ID"] = request_id
    return response


def _error(status: int, error: str, detail) -> JSONResponse:
    return JSONResponse(status_code=status, content=ErrorResponse(error=error, detail=detail).model_dump())


@app.exception_handler(RequestValidationError)
async def validation_error(_: Request, exc: RequestValidationError):
    detail = [{"field": ".".join(str(p) for p in e["loc"] if p != "body") or "body", "message": e["msg"]}
              for e in exc.errors()]
    return _error(422, "validation_error", detail)


@app.exception_handler(StarletteHTTPException)
async def http_error(_: Request, exc: StarletteHTTPException):
    return _error(exc.status_code, ERROR_CODES.get(exc.status_code, "http_error"), exc.detail)


@app.exception_handler(Exception)
async def unexpected_error(_: Request, exc: Exception):
    log.error("Unexpected error: %s", type(exc).__name__)
    return _error(500, "internal_error", "An unexpected error occurred. Check the server log for the error type.")


# ----------------------------------------------------------------------------- dependencies
def chat_model() -> BaseChatModel:
    """The chat model for this request; 503 when the provider is not usable. Tests can override it."""
    settings = get_settings()
    if problem := provider_problem(settings):
        raise HTTPException(status_code=503, detail=problem)
    return get_chat_model(settings)


# ----------------------------------------------------------------------------- endpoints
@app.get("/", include_in_schema=False)
def home():
    return {"message": "AI Learning Assistant is running.", "docs": "/docs", "health": "/health"}


@app.get("/health", response_model=HealthResponse, tags=["status"])
def health():
    """Application status, the configured provider and model, and LangSmith tracing status."""
    settings = get_settings()
    problem = provider_problem(settings)
    return HealthResponse(status="degraded" if problem else "ok", version=__version__,
                          llm_provider=settings.llm_provider, model=settings.model_name, problem=problem,
                          langsmith=configure_tracing(settings))


@app.post("/ask", response_model=AskResponse, tags=["learning"],
          responses={**ERROR_RESPONSES, 502: {"model": ErrorResponse, "description": "The model failed or returned invalid output"}})
def ask(body: QuestionRequest, model: BaseChatModel = Depends(chat_model)):
    """**LangChain alone** — one prompt template, one model call, one structured answer."""
    settings = get_settings()
    config, _ = run_config("learning-ask", ["langchain", "ask"], {"provider": settings.llm_provider})
    try:
        answer = answer_question(body.question, model, config=config)
    except OutputParserException:
        log.warning("/ask: model output did not match the schema")
        raise HTTPException(status_code=502, detail="The model's reply did not match the expected format. "
                                                    "Try again, use /workflow (it retries and falls back), or use mock mode.")
    except Exception as exc:
        log.warning("/ask: model call failed (%s)", type(exc).__name__)
        raise HTTPException(status_code=502, detail="The language model could not be reached or failed. "
                                                    "Check the LLM_PROVIDER settings, or use mock mode.")
    return AskResponse(question=body.question, topic=answer.topic, explanation=answer.explanation,
                       example=answer.example, status="success", mode=settings.llm_provider,
                       note=MOCK_NOTE if settings.llm_provider == "mock" else None)


@app.post("/workflow", response_model=WorkflowResponse, tags=["learning"], responses=ERROR_RESPONSES)
def workflow(body: QuestionRequest, model: BaseChatModel = Depends(chat_model)):
    """**LangGraph workflow** — classify, explain, add an example, validate; retry once, then fall back."""
    settings = get_settings()
    tracing = configure_tracing(settings)
    return run_workflow(body.question, settings=settings, model=model, tracing_enabled=tracing["enabled"])


# ----------------------------------------------------------------------------- branded docs page
@app.get("/docs", include_in_schema=False)
def docs():
    return get_swagger_ui_html(openapi_url=app.openapi_url, title=app.title + " - Docs",
                               swagger_favicon_url="/brand/logo.png")


@app.get("/brand/{name}", include_in_schema=False)
def brand_image(name: str):
    """Serves only the two brand images used on the docs page."""
    path = BRAND_FILES.get(name)
    if path is None or not path.exists():
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(path, media_type="image/png")
