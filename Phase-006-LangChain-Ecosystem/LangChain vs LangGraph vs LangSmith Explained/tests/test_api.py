"""FastAPI endpoints: success, validation errors, provider and model failures, docs."""
import pytest
from fastapi.testclient import TestClient

from app.llm import MockChatModel
from app.main import app, chat_model
from app.schemas import AskResponse, ErrorResponse, HealthResponse, WorkflowResponse

QUESTION = {"question": "What is Agentic AI? Explain with a simple real-world example."}


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    body = HealthResponse(**response.json())
    assert body.status == "ok" and body.llm_provider == "mock" and body.langsmith.enabled is False
    assert response.headers["X-Request-ID"]


def test_ask_success(client):
    response = client.post("/ask", json=QUESTION)
    assert response.status_code == 200
    body = AskResponse(**response.json())
    assert body.topic == "Agentic AI" and body.status == "success" and body.mode == "mock" and body.note


def test_workflow_success(client):
    response = client.post("/workflow", json=QUESTION)
    assert response.status_code == 200
    body = WorkflowResponse(**response.json())
    assert body.status == "success" and body.steps[-1] == "finalize" and body.key_points


@pytest.mark.parametrize("payload, field", [
    ({"question": "   "}, "question"),          # blank
    ({"question": "AI"}, "question"),           # too short
    ({"question": "x" * 501}, "question"),      # too long
    ({}, "question"),                           # missing field
    ({"question": 42}, "question"),             # wrong type
])
@pytest.mark.parametrize("endpoint", ["/ask", "/workflow"])
def test_invalid_requests_return_consistent_422(client, endpoint, payload, field):
    response = client.post(endpoint, json=payload)
    assert response.status_code == 422
    body = ErrorResponse(**response.json())
    assert body.error == "validation_error" and body.detail[0]["field"] == field


def test_unknown_provider_returns_503(client, monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "unknown")
    for endpoint in ("/ask", "/workflow"):
        response = client.post(endpoint, json=QUESTION)
        assert response.status_code == 503 and response.json()["error"] == "service_unavailable"
    assert client.get("/health").json()["status"] == "degraded"


def test_openai_without_key_returns_503(client, monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    response = client.post("/ask", json=QUESTION)
    assert response.status_code == 503 and "OPENAI_API_KEY" in response.json()["detail"]


def test_ask_model_failure_returns_502_without_internals(client):
    app.dependency_overrides[chat_model] = lambda: MockChatModel(fail_times=10)
    response = client.post("/ask", json=QUESTION)
    assert response.status_code == 502 and response.json()["error"] == "model_error"
    assert "Simulated" not in response.text and "Traceback" not in response.text


def test_ask_invalid_model_output_returns_502(client):
    app.dependency_overrides[chat_model] = lambda: MockChatModel(invalid_times=10)
    response = client.post("/ask", json=QUESTION)
    assert response.status_code == 502 and "format" in response.json()["detail"]


def test_workflow_model_failure_falls_back(client):
    app.dependency_overrides[chat_model] = lambda: MockChatModel(fail_times=10)
    response = client.post("/workflow", json=QUESTION)
    assert response.status_code == 200 and response.json()["status"] == "fallback"


def test_docs_and_openapi(client):
    assert client.get("/docs").status_code == 200
    spec = client.get("/openapi.json").json()
    assert {"/health", "/ask", "/workflow"} <= set(spec["paths"])
    assert "ErrorResponse" in spec["components"]["schemas"]


def test_brand_route_only_serves_known_files(client):
    assert client.get("/brand/logo.png").status_code == 200
    assert client.get("/brand/..%2Fapp%2Fmain.py").status_code == 404
