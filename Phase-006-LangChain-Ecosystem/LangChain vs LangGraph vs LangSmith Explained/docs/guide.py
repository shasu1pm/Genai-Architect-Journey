"""Content and layout of the two PDFs (called by build_docs.py).

- docs/LangChain-LangGraph-LangSmith-Guide.pdf                — the complete guide, with a contents page
- LangChain-vs-LangGraph-vs-LangSmith-Explained-Explainer.pdf  — the short explainer for this folder

The brand engine (cover, header, footer, typography) comes from zz-Brand-Assets/pdf-kit/brand_pdf.py.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from build_docs import DOCS, INFOGRAPHIC, PROJECT, REPO

sys.path.insert(0, str(REPO / "zz-Brand-Assets" / "pdf-kit"))
from brand_pdf import (LM, RM, W, KeepTogether, Paragraph, S, Spacer, build, bullets, callout, code,  # noqa: E402
                       flow, h1, h2, lead, p, small, table)
from reportlab.platypus import Image  # noqa: E402

FOLDER = "Phase-006-LangChain-Ecosystem"
GUIDE = DOCS / "LangChain-LangGraph-LangSmith-Guide.pdf"
EXPLAINER = PROJECT / "LangChain-vs-LangGraph-vs-LangSmith-Explained-Explainer.pdf"
AVAIL = W - LM - RM
ATTRIBUTION = "This educational project is independently developed and maintained by Shasu Vathanan."
REFERENCES = [
    ["LangChain", "https://docs.langchain.com/oss/python/langchain/overview"],
    ["LangGraph", "https://docs.langchain.com/oss/python/langgraph/overview"],
    ["LangSmith", "https://docs.langchain.com/langsmith/"],
    ["LangSmith evaluation", "https://docs.langchain.com/langsmith/evaluation"],
    ["LangChain docs home", "https://docs.langchain.com/"],
    ["FastAPI", "https://fastapi.tiangolo.com/"],
    ["Pydantic", "https://docs.pydantic.dev/latest/"],
    ["Python", "https://docs.python.org/3/"],
    ["Ollama", "https://docs.ollama.com/"],
]


def figure(path: Path, caption: str, width: float = AVAIL, max_height: float = 600):
    from PIL import Image as PILImage
    with PILImage.open(path) as im:
        w, h = im.size
    width = min(width, max_height * w / h)
    img = Image(str(path), width=width, height=width * h / w)
    img.hAlign = "CENTER"
    return [KeepTogether([img, Spacer(1, 4), small(caption)]), Spacer(1, 6)]


def kcode(text: str, title: str | None = None) -> list:
    """A code block that never splits from its title across pages."""
    return [KeepTogether(code(text, title))]


def with_heading(heading: str, first_block: list) -> list:
    """Keep a section heading on the same page as the block that follows it."""
    return [KeepTogether(h1(heading) + first_block)]


def sample_calls() -> list[dict]:
    return json.loads((PROJECT / "examples" / "sample_responses.json").read_text(encoding="utf-8"))["calls"]


def short_json(obj: dict, limit: int = 58) -> str:
    """Pretty JSON with long strings shortened, so the example fits on a page."""
    def cut(v):
        if isinstance(v, str) and len(v) > limit:
            return v[:limit].rsplit(" ", 1)[0] + " …"
        if isinstance(v, list):
            return [cut(x) for x in v]
        if isinstance(v, dict):
            return {k: cut(x) for k, x in v.items()}
        return v
    return json.dumps(cut(obj), indent=2, ensure_ascii=False)


# ----------------------------------------------------------------------------- shared sections
def section_three_tools() -> list:
    s = []
    s += h1("LangChain fundamentals")
    s.append(lead("LangChain is the building kit: standard parts for talking to language models."))
    s.append(p("LangChain is an open-source framework for building applications with language models. Instead of "
               "writing provider-specific code, you work with standard components — **chat models**, **prompt "
               "templates**, **output parsers**, **tools** and **retrievers** — and join them with **LCEL** (the "
               "LangChain Expression Language), written with the `|` operator."))
    s += table(["Component", "What it does", "In this project"], [
        ["Chat model", "One interface for many providers", "`app/llm.py` — mock, OpenAI or Ollama"],
        ["Prompt template", "Fills variables into chat messages", "`ChatPromptTemplate` in `app/chains.py`"],
        ["Output parser", "Turns text into a typed object, or fails clearly", "`PydanticOutputParser`"],
        ["Chain (LCEL)", "prompt | model | parser", "explain, example and answer chains"],
    ], [0.22, 0.4, 0.38])
    s.append(p("**Why it helps:** switching provider is a configuration change, prompts are reusable, and "
               "structured output turns a free-text reply into data your API can trust."))
    s.append(p("**Grounding:** for topics the project knows, the prompt adds short background notes from "
               "`app/knowledge.py`; the model writes its own answer but takes its facts from them. The expected reply "
               "is shown as a short JSON template, which small local models follow far more reliably than a full schema."))

    s += h1("LangGraph fundamentals")
    s.append(lead("LangGraph is the control room: it decides which step runs next and keeps the shared state."))
    s.append(p("LangGraph is an open-source framework for **stateful, multi-step workflows** expressed as a graph. "
               "You define a **state** (a typed dictionary), **nodes** (Python functions that update the state) and "
               "**edges** (what runs next). **Conditional edges** call a small Python function to pick the next node, "
               "which makes branching, loops with limits, retries and human approval explicit and testable."))
    s += table(["Term", "Meaning", "In this project"], [
        ["State", "Data shared by every node", "`LearningState` — question, topic, explanation, attempts, steps …"],
        ["Node", "One step of work", "receive · classify · clarify · explain · add_example · validate · fallback · finalize"],
        ["Edge", "A fixed next step", "explain → add_example → validate"],
        ["Conditional edge", "A Python function chooses", "`route_after_classify`, `route_after_validate`"],
        ["Compile", "Turns the definition into a runnable app", "`graph.compile()` then `.invoke()`"],
    ], [0.2, 0.32, 0.48])
    s += callout("LangGraph does not require LangChain",
                 "Any Python function can be a node. In this project four nodes are plain Python (classify, validate, "
                 "fallback, finalize) and two call LangChain chains (explain, add_example). The two libraries work "
                 "well together, but neither is a mandatory step for the other.", "tip")

    s += h1("LangSmith fundamentals")
    s.append(lead("LangSmith is the flight recorder: it shows what happened inside every run."))
    s.append(p("LangSmith is a hosted platform for **observing, debugging and evaluating** LLM applications. With "
               "tracing switched on, each run is stored as a **run tree** — the workflow, every node, every model "
               "call — with inputs, outputs, errors, latency and token usage. **Datasets** and **evaluators** let you "
               "score answers and compare versions over time."))
    s += bullets(["**Optional:** the application behaves the same with tracing on or off.",
                  "**Hosted:** it needs a LangSmith account, an API key, internet access, and is subject to the plan's limits.",
                  "**Not an execution engine:** LangSmith records and evaluates runs; it does not run your workflow."])
    return s


def section_comparison(with_image: bool = True, image: Path | None = None) -> list:
    s = []
    s += h1("LangChain vs LangGraph vs LangSmith")
    s += table(["", "LangChain", "LangGraph", "LangSmith"], [
        ["Remember it as", "**Build**", "**Orchestrate**", "**Observe**"],
        ["What it is", "Framework for LLM application components", "Framework for stateful workflow graphs",
         "Hosted tracing and evaluation platform"],
        ["Core ideas", "Chat models, prompts, parsers, tools, LCEL", "State, nodes, edges, conditional routing",
         "Traces, run trees, datasets, evaluators"],
        ["Use it when", "One or a few model calls with clear input and output",
         "Step order matters: branching, retries, approvals, long-running state",
         "You need to see why an answer happened, what it cost and how long it took"],
        ["Runs your code?", "Yes", "Yes", "No — it observes"],
        ["In this project", "`/ask` and the explain/example chains", "`/workflow`", "Optional tracing and `examples/evaluate.py`"],
    ], [0.17, 0.27, 0.28, 0.28])
    s += table(["Situation", "Good choice"], [
        ["Summarise an email into three bullet points", "LangChain alone — one chain"],
        ["Answer, check the answer, retry once, otherwise use a safe fallback", "LangGraph (with LangChain chains inside nodes)"],
        ["A user reports a wrong answer and you need to know which step caused it", "LangSmith trace of that run"],
        ["You changed a prompt and want proof it did not make answers worse", "LangSmith evaluation on a dataset"],
    ], [0.62, 0.38])
    if with_image:
        s += figure(image or INFOGRAPHIC, "LangChain vs LangGraph vs LangSmith — with FastAPI and Python (assets/comparison.svg).",
                    max_height=560)
    return s


def section_fastapi_python() -> list:
    s = []
    s += h1("FastAPI and Python")
    s.append(p("**FastAPI** is a Python web framework for HTTP APIs. Request and response shapes are Pydantic models, "
               "so FastAPI validates input automatically, returns clear errors and generates the **OpenAPI** "
               "specification and an interactive **Swagger UI**. **Python** is the implementation environment for "
               "everything: configuration, logging, the chains, the graph, the API and the tests."))
    s += table(["Concern", "How it is handled"], [
        ["Validation", "`QuestionRequest`: 3–500 characters after trimming; blank, missing or wrong type → 422"],
        ["Errors", "One shape for every error: `{\"status\": \"error\", \"error\": code, \"detail\": …}`"],
        ["Status codes", "200 success · 422 invalid request · 502 model failed (/ask) · 503 provider not usable"],
        ["Logging", "Method, path, status, duration and a request id — no bodies, no headers; keys are masked"],
        ["Docs", "Swagger UI at `/docs`, specification at `/openapi.json`"],
    ], [0.2, 0.8])
    return s


def section_references() -> list:
    s = []
    s += h1("References & Documentation")
    s += table(["Topic", "Official documentation"], REFERENCES, [0.25, 0.75])
    s.append(p(ATTRIBUTION))
    s += table(["Library", "Licence (from package metadata)"], [
        ["langchain · langchain-core · langchain-openai · langchain-ollama", "MIT"],
        ["langgraph · langsmith (SDK) · fastapi · pydantic · pytest", "MIT"],
        ["uvicorn · python-dotenv · httpx · starlette", "BSD-3-Clause"],
    ], [0.7, 0.3])
    s.append(small("Libraries are installed from requirements.txt and are not copied into the repository."))
    return s


# ----------------------------------------------------------------------------- full guide
def guide_story(img: dict[str, Path], toc_pages: dict[str, str]) -> list:
    calls = sample_calls()
    s = []
    s += h1("Contents")
    titles = ["Project overview and learning objectives", "LangChain fundamentals", "LangGraph fundamentals",
              "LangSmith fundamentals", "LangChain vs LangGraph vs LangSmith", "FastAPI and Python",
              "System architecture", "End-to-end workflow", "Implementation — the Python modules",
              "Windows 11 setup", "Configuration, mock mode and real LLM mode", "API demonstration",
              "LangSmith tracing and evaluation", "Testing and validation", "Troubleshooting", "Key takeaways",
              "References & Documentation", "About the author"]
    s += table(["#", "Section", "Page"], [[str(i), t, toc_pages.get(t, "–")] for i, t in enumerate(titles, 1)],
               [0.08, 0.8, 0.12])

    s += h1("Project overview and learning objectives")
    s.append(lead("An AI Learning Assistant that turns a question into a beginner-friendly explanation with a real-world example."))
    s.append(p("The project answers questions such as \"What is Agentic AI? Explain with a simple real-world example.\" "
               "It is small enough to read in an afternoon, yet it uses each technology for the job it is best at: "
               "**LangChain** builds the model calls, **LangGraph** orchestrates the steps, **LangSmith** observes them, "
               "**FastAPI** serves them and **Python** ties everything together. A deterministic **mock mode** makes it "
               "run anywhere — no paid API and no account needed."))
    s += bullets(["Explain what LangChain, LangGraph and LangSmith each do — and how they relate.",
                  "Build structured LangChain chains: prompt template, chat model, output parser.",
                  "Design a LangGraph workflow with state, conditional routing, a bounded retry and a fallback.",
                  "Add optional LangSmith tracing and a small evaluation.",
                  "Serve it with FastAPI: validation, status codes, consistent errors, Swagger UI.",
                  "Test everything offline with pytest."])

    s += section_three_tools()
    s += section_comparison(image=img.get("comparison"))
    s += section_fastapi_python()

    s += h1("System architecture")
    s += figure(img["architecture"], "System architecture (assets/architecture.svg).")
    s.append(p("A client calls FastAPI. **/ask** runs one LangChain chain on its own. **/workflow** runs the LangGraph "
               "workflow, whose explain and add_example nodes call LangChain chains. Every chain talks to the chat model "
               "chosen by `LLM_PROVIDER`. When tracing is enabled, both kinds of run are recorded in LangSmith."))

    s += h1("End-to-end workflow")
    s += figure(img["workflow"], "The LangGraph workflow behind POST /workflow (assets/workflow.svg).")
    s += table(["#", "Step", "Where"], [
        ["1", "Receive the request", "FastAPI `POST /workflow`"],
        ["2", "Validate input (3–500 characters)", "Pydantic `QuestionRequest`"],
        ["3", "Initialise the workflow state", "node **receive**"],
        ["4", "Classify topic and explanation type (concept, comparison, how-to, small talk)", "node **classify** — plain Python"],
        ["5", "Prepare a prompt from a reusable template", "`ChatPromptTemplate` in the explain chain"],
        ["6", "Invoke the chat model and parse the structured reply", "node **explain** — LangChain"],
        ["7", "Generate a practical real-world example", "node **add_example** — LangChain"],
        ["8", "Check explanation, key points and example are present", "node **validate**"],
        ["9", "Retry once (bounded), then fall back to a predefined answer", "`route_after_validate` → explain or **fallback**"],
        ["10", "Record the run when tracing is enabled", "LangSmith (optional)"],
        ["11", "Build the validated JSON response", "node **finalize** + `WorkflowResponse`"],
        ["12", "Return the result", "FastAPI → HTTP 200"],
    ], [0.06, 0.6, 0.34])
    s.append(p("Small talk such as \"Hello!\" is routed to **clarify**, which asks for a learning question — a second "
               "conditional route. Because the retry count is capped by `MAX_RETRIES`, the graph always reaches END."))

    s += h1("Implementation — the Python modules")
    s += table(["File", "Responsibility"], [
        ["`app/config.py`", "Settings from `.env`, provider checks, logging with secret redaction"],
        ["`app/schemas.py`", "Pydantic models for requests, model outputs and API responses"],
        ["`app/knowledge.py`", "Deterministic classifier and the predefined answers used by mock mode and fallback"],
        ["`app/llm.py`", "Chat-model factory (mock, OpenAI, Ollama) and the deterministic `MockChatModel`"],
        ["`app/chains.py`", "LangChain prompt templates and chains"],
        ["`app/graph.py`", "LangGraph state, nodes, conditional routing and `run_workflow`"],
        ["`app/observability.py`", "Optional LangSmith tracing and run ids"],
        ["`app/main.py`", "FastAPI app: endpoints, error handlers, request logging, branded docs page"],
        ["`tests/`", "pytest suite — API and workflow (offline) and opt-in real-model tests"],
        ["`examples/`", "Sample requests, recorded mock and real-model (Ollama) responses, evaluation script"],
    ], [0.3, 0.7])
    s += kcode('''_EXPLAIN_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "TASK=explain\\n" + TUTOR + "\\n{style}\\nReturn only JSON.\\n{format_instructions}"),
    ("human", "Topic: {topic}\\nQuestion: {question}"),
])
parser = PydanticOutputParser(pydantic_object=Explanation)
chain = _EXPLAIN_PROMPT.partial(format_instructions=parser.get_format_instructions()) | model | parser''',
              "app/chains.py — a LangChain chain with structured output")
    s += kcode('''graph.add_conditional_edges("classify", route_after_classify, {"clarify": "clarify", "explain": "explain"})
graph.add_edge("explain", "add_example")
graph.add_edge("add_example", "validate")
graph.add_conditional_edges("validate", route_after_validate,
                            {"finalize": "finalize", "explain": "explain", "fallback": "fallback"})

def route_after_validate(state):
    if not state["validation_errors"]:
        return "finalize"
    if state["attempts"] < state["max_attempts"]:
        return "explain"          # bounded retry
    return "fallback"''', "app/graph.py — conditional routing with a bounded retry")

    s += with_heading("Windows 11 setup", kcode('''# 1. Python 3.10 or newer (python.org — tick "Add python.exe to PATH")
python --version

# 2. Open PowerShell in the project folder (quotes are needed: the path has spaces)
cd "Phase-006-LangChain-Ecosystem\\LangChain vs LangGraph vs LangSmith Explained"

# 3. Virtual environment and dependencies
python -m venv .venv
.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 4. Configuration (mock mode by default — no key needed)
copy .env.example .env

# 5. Tests, then the API
python -m pytest
uvicorn app.main:app --reload          # open http://127.0.0.1:8000/docs''', "PowerShell"))
    s.append(small("If PowerShell blocks Activate.ps1, run Set-ExecutionPolicy -Scope CurrentUser RemoteSigned once, "
                   "or use Command Prompt with .venv\\Scripts\\activate.bat."))

    s += h1("Configuration, mock mode and real LLM mode")
    s += table(["Variable", "Default", "Purpose"], [
        ["`LLM_PROVIDER`", "mock", "mock · openai · ollama"],
        ["`OPENAI_API_KEY` / `OPENAI_MODEL`", "— / gpt-4.1-mini", "OpenAI access and model"],
        ["`OLLAMA_MODEL` / `OLLAMA_BASE_URL`", "qwen2.5:0.5b / localhost:11434", "Local model served by Ollama"],
        ["`LLM_TEMPERATURE`", "0.2", "Lower = more focused answers"],
        ["`MAX_RETRIES`", "1", "Extra attempts when validation fails (0–3)"],
        ["`LANGSMITH_TRACING` / `LANGSMITH_API_KEY` / `LANGSMITH_PROJECT`", "false / — / ai-learning-assistant", "Optional tracing"],
        ["`LOG_LEVEL`", "INFO", "Logging detail"],
    ], [0.42, 0.28, 0.3])
    s += table(["Mode", "How", "What you get"], [
        ["**Mock** (default)", "`LLM_PROVIDER=mock`", "Predefined answers for core AI topics, always the same, labelled "
                                                          "\"Mock mode: a predefined sample answer, not generated by a language model.\""],
        ["**OpenAI**", "`LLM_PROVIDER=openai` + `OPENAI_API_KEY`", "Generated answers; paid per token"],
        ["**Ollama** (local)", "Install Ollama, `ollama pull qwen2.5:0.5b`, `LLM_PROVIDER=ollama`",
         "Free, local generation — tested with qwen2.5:0.5b"],
    ], [0.18, 0.37, 0.45])
    s += callout("Tested with a real local model",
                 "Ollama 0.17.1 with qwen2.5:0.5b on Windows 11: 24 real requests (4 questions × /ask and /workflow × 3 "
                 "rounds) all returned HTTP 200 with status success, the workflow finishing on its first attempt, in "
                 "5–13 seconds each once the model was loaded. A 0.5B model sometimes repeats the background notes "
                 "almost word for word and can be imprecise — use a larger model or OpenAI when accuracy matters.", "tip")

    s += h1("API demonstration")
    s += table(["Method", "Endpoint", "Purpose"], [
        ["GET", "`/health`", "Application, provider and LangSmith status"],
        ["POST", "`/ask`", "LangChain alone — one chain, one model call"],
        ["POST", "`/workflow`", "The complete LangGraph workflow"],
        ["GET", "`/docs` · `/openapi.json`", "Swagger UI · OpenAPI specification"],
    ], [0.12, 0.3, 0.58])
    ask, wf = calls[1], calls[2]
    s += kcode('POST /ask\n' + json.dumps(ask["request"]["json"], indent=2) + "\n\nHTTP 200\n" + short_json(ask["response"]),
              "Recorded response — mock mode")
    s += kcode('POST /workflow\n' + json.dumps(wf["request"]["json"]) + "\n\nHTTP 200\n" + short_json(
        {k: wf["response"][k] for k in ("topic", "question_type", "status", "mode", "steps", "attempts",
                                        "validation_errors", "trace_id")}), "Recorded response — fields of interest")
    bad = calls[-1]
    s += kcode('POST /ask\n' + json.dumps(bad["request"]["json"]) + f"\n\nHTTP {bad['status_code']}\n"
              + json.dumps(bad["response"], indent=2), "Validation error — consistent error format")

    s += h1("LangSmith tracing and evaluation")
    s += kcode('''LANGSMITH_TRACING="true"
LANGSMITH_API_KEY="your_langsmith_api_key"
LANGSMITH_PROJECT="ai-learning-assistant"''', ".env")
    s += bullets([
        "Restart the server; `/health` shows `\"langsmith\": {\"enabled\": true, …}`.",
        "Each `/workflow` response then carries a `trace_id` — the LangSmith run id — so the exact run can be found.",
        "The run tree shows every node and model call with inputs, outputs, errors and latency; tags are `langgraph`, "
        "`workflow` (or `langchain`, `ask`), with the provider and model as metadata.",
        "`python examples/evaluate.py` scores the workflow locally (topic, status, example). Add `--langsmith` to upload "
        "the dataset and create a LangSmith experiment.",
        "Without a key, tracing is switched off with a clear reason and the application keeps working.",
    ])

    s += h1("Testing and validation")
    s += table(["Area", "What the tests check"], [
        ["LangChain", "Each chain returns its Pydantic type; mock output is deterministic"],
        ["LangGraph", "Node order, state passing, both conditional routes, one retry then success, bounded "
                      "retries then fallback, `MAX_RETRIES` respected, every node present in the graph"],
        ["LangSmith", "Off without a key (with a reason), on with a key; the app still works when off"],
        ["FastAPI", "200 for /health, /ask, /workflow; 422 for blank, short, long, missing and wrong-type questions on "
                    "both endpoints; 503 for an unusable provider; 502 for model failure and invalid output; "
                    "fallback on /workflow; /docs and /openapi.json"],
        ["Safety", "API keys are masked in logs; error bodies contain no internal details; the brand route serves only two files"],
    ], [0.18, 0.82])
    s += kcode("python -m pytest              # offline, mock mode\n38 passed\n\n"
               "python -m pytest -m ollama    # real model: qwen2.5:0.5b through Ollama\n4 passed",
               "Results on Windows 11, Python 3.13")

    s += h1("Troubleshooting")
    s += table(["Problem", "Fix"], [
        ["`uvicorn` is not recognised", "Activate the virtual environment, or run `python -m uvicorn app.main:app --reload`"],
        ["Activate.ps1 cannot be loaded", "`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, or use `activate.bat` in Command Prompt"],
        ["`No module named 'app'`", "Run commands from the project folder (the one with `pyproject.toml`)"],
        ["503 — needs OPENAI_API_KEY", "Add the key to `.env`, or set `LLM_PROVIDER=mock`"],
        ["502 from /ask with Ollama", "Start Ollama, run `ollama pull qwen2.5:0.5b`, check `OLLAMA_MODEL`"],
        ["/workflow returns status fallback", "The model's answers failed validation twice; try a larger model or `MAX_RETRIES=2`"],
        ["LangSmith shows nothing", "Set `LANGSMITH_TRACING=true` and `LANGSMITH_API_KEY`, restart, check `/health`"],
        ["Small local model repeats the notes or is imprecise", "Expected with a 0.5B model; use `qwen2.5:3b` or larger, or OpenAI"],
        ["Port 8000 is busy", "`uvicorn app.main:app --reload --port 8001`"],
    ], [0.36, 0.64])

    s += h1("Key takeaways")
    s += bullets(["**LangChain builds** the model calls: prompt templates, chat models and structured output.",
                  "**LangGraph orchestrates** the steps: state, routing, bounded retries and fallbacks in plain Python.",
                  "**LangSmith observes** and evaluates — optional, never required to run the app.",
                  "**FastAPI serves** it with validation, clear status codes and generated documentation.",
                  "**Python** holds it together — and a deterministic mock mode makes everything testable."])

    s += section_references()

    s += h1("About the author")
    s.append(p("**Shasu Vathanan - GEN AI - Product Manager** — this guide, the AI Learning Assistant, its explanations, "
               "examples and diagrams are developed and maintained by Shasu Vathanan as part of the GenAI Architect Journey."))
    s += table(["", ""], [["Website", "SHASUVATHANAN.COM — https://shasuvathanan.com"],
                          ["LinkedIn", "https://www.linkedin.com/in/shasuvathanan"],
                          ["GitHub", "https://github.com/shasu1pm/Genai-Architect-Journey"]], [0.2, 0.8])
    return s, titles


# ----------------------------------------------------------------------------- explainer
def explainer_story(img: dict[str, Path]) -> list:
    s = []
    s += h1("What this folder is")
    s.append(lead("One working project that shows what LangChain, LangGraph and LangSmith each do — served with FastAPI."))
    s.append(p("The **AI Learning Assistant** answers educational questions with a beginner-friendly explanation and a "
               "real-world example. It runs in a deterministic **mock mode** without any key, or with OpenAI or a local "
               "Ollama model. The complete guide is `docs/LangChain-LangGraph-LangSmith-Guide.pdf`."))
    s += flow(["FastAPI receives", "classify", "explain (LangChain)", "add example", "validate", "retry or fallback", "JSON reply"])
    s += section_comparison(with_image=False)
    s += with_heading("Architecture and workflow", figure(img["architecture"], "System architecture.", max_height=300))
    s += figure(img["workflow"], "LangGraph workflow with conditional routing, bounded retry and fallback.", max_height=300)
    s += h1("Run it")
    s += kcode('''cd "Phase-006-LangChain-Ecosystem\\LangChain vs LangGraph vs LangSmith Explained"
python -m venv .venv
.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
copy .env.example .env               # mock mode by default
python -m pytest                     # offline tests
uvicorn app.main:app --reload        # http://127.0.0.1:8000/docs''', "Windows 11 — PowerShell")
    s += table(["Endpoint", "What it does"], [
        ["GET `/health`", "Status, provider, model and LangSmith tracing"],
        ["POST `/ask`", "LangChain alone — one prompt, one model call, one structured answer"],
        ["POST `/workflow`", "LangGraph — classify, explain, example, validate, bounded retry, fallback"],
    ], [0.3, 0.7])
    s += h1("Key takeaways")
    s += bullets(["LangChain **builds**, LangGraph **orchestrates**, LangSmith **observes** — complementary, not a required sequence.",
                  "Keep routing, retries and fallbacks in code when they must be reliable.",
                  "Tracing is optional, but it is the fastest way to see why an answer happened."])
    s.append(small(ATTRIBUTION))
    return s


def _optimise(src: Path, dst: Path | None = None, max_width: int = 2400) -> Path:
    """A smaller copy for the PDF only: limited width and a 256-colour palette (diagrams are flat colour)."""
    from PIL import Image as PILImage
    dst = dst or src
    with PILImage.open(src) as im:
        im = im.convert("RGB")
        if im.width > max_width:
            im = im.resize((max_width, round(im.height * max_width / im.width)), PILImage.LANCZOS)
        im.quantize(colors=256, method=PILImage.Quantize.MEDIANCUT).save(dst, "PNG", optimize=True)
    return dst


def _pages_of(pdf: Path, titles: list[str]) -> dict[str, str]:
    import fitz
    doc = fitz.open(pdf)
    found = {}
    for title in titles:
        seen = 0                                        # the first match is the contents entry itself
        for i in range(1, doc.page_count):
            seen += [l.strip() for l in doc[i].get_text().splitlines()].count(title)
            if seen >= 2:
                found[title] = str(i + 1)
                break
    return found


def build_pdfs(svgs: dict[str, Path], render_png) -> None:
    import fitz
    with tempfile.TemporaryDirectory() as tmp:
        img = {name: _optimise(render_png(svgs[f"{name}.svg"], Path(tmp) / f"{name}.png", scale=1.5))
               for name in ("architecture", "workflow")}
        img["comparison"] = _optimise(INFOGRAPHIC, Path(tmp) / "comparison.png", max_width=1600)
        common = dict(folder=FOLDER, keywords="LangChain, LangGraph, LangSmith, FastAPI, Python, AI Learning Assistant")
        story, titles = guide_story(img, {})
        facts = [("Document", "Complete project guide"), ("Project", "AI Learning Assistant"),
                 ("Stack", "LangChain · LangGraph · LangSmith · FastAPI · Python"),
                 ("Runs", "Mock mode (no key) · OpenAI · Ollama"), ("Folder", f"{FOLDER} / LangChain vs LangGraph vs LangSmith Explained")]
        args = dict(title="LangChain vs LangGraph vs LangSmith Guide", short="LangChain · LangGraph · LangSmith Guide",
                    subtitle="Build, orchestrate and observe an AI Learning Assistant with FastAPI and Python", facts=facts, **common)
        build(GUIDE, story=story, **args)
        pages = _pages_of(GUIDE, titles)                  # second pass: real page numbers in the contents
        story, _ = guide_story(img, pages)
        build(GUIDE, story=story, **args)
        build(EXPLAINER, story=explainer_story(img), title="LangChain vs LangGraph vs LangSmith Explained",
              short="LangChain vs LangGraph vs LangSmith",
              subtitle="Build · Orchestrate · Observe — the AI Learning Assistant in a short guide",
              facts=[("Document", "Folder explainer"), ("Project", "AI Learning Assistant"),
                     ("Stack", "LangChain · LangGraph · LangSmith · FastAPI · Python"),
                     ("Full guide", "docs/LangChain-LangGraph-LangSmith-Guide.pdf"),
                     ("Folder", f"{FOLDER} / LangChain vs LangGraph vs LangSmith Explained")], **common)
    for pdf in (GUIDE, EXPLAINER):
        n = fitz.open(pdf).page_count
        print(f"pdf  {pdf.relative_to(PROJECT)}  {n} pages{'  ** OVER 15 **' if n > 15 else ''}")
    missing = [t for t in titles if t not in pages]
    if missing:
        print("contents: sections not found:", missing)
