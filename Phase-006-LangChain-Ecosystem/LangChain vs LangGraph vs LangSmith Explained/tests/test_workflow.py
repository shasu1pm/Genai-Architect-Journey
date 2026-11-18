"""LangChain chains, the LangGraph workflow, the mock model and observability settings."""
import logging

import pytest

from app.chains import build_answer_chain, build_example_chain, build_explain_chain
from app.config import SecretRedactingFilter, get_settings
from app.graph import route_after_validate, run_workflow, workflow_mermaid
from app.knowledge import classify_question
from app.llm import MOCK_NOTE, MockChatModel
from app.observability import configure_tracing
from app.schemas import Explanation, LearningAnswer, PracticalExample, WorkflowResponse

MAIN_PATH = ["receive", "classify", "explain", "add_example", "validate", "finalize"]


@pytest.mark.parametrize("question, topic, kind", [
    ("What is Agentic AI? Explain with a simple real-world example.", "Agentic AI", "concept"),
    ("LangChain vs LangGraph: what is the difference?", "LangChain vs LangGraph", "comparison"),
    ("How do I build an API with FastAPI?", "FastAPI", "how_to"),
    ("Hello!", "Small talk", "small_talk"),
    ("What is quantum computing?", "Quantum computing", "concept"),
])
def test_classifier(question, topic, kind):
    assert classify_question(question) == {"topic": topic, "question_type": kind}


def test_chains_return_structured_objects():
    model = MockChatModel()
    explained = build_explain_chain(model).invoke({"topic": "LangGraph", "question": "What is LangGraph?",
                                                   "style": "Explain it.", "notes": "none"})
    assert isinstance(explained, Explanation) and explained.topic == "LangGraph" and explained.key_points
    example = build_example_chain(model).invoke({"topic": "LangGraph", "explanation": explained.explanation})
    assert isinstance(example, PracticalExample) and len(example.example.split()) > 8
    answer = build_answer_chain(model).invoke({"topic": "Agentic AI", "question": "What is Agentic AI?",
                                               "notes": "none"})
    assert isinstance(answer, LearningAnswer) and "travel" in answer.example


def test_success_path_runs_nodes_in_order_and_matches_schema():
    result = run_workflow("What is Agentic AI? Explain with a simple real-world example.")
    WorkflowResponse(**result)                       # raises if the structure is wrong
    assert result["steps"] == MAIN_PATH
    assert result["status"] == "success" and result["attempts"] == 1 and result["validation_errors"] == []
    assert result["topic"] == "Agentic AI" and "travel" in result["example"]
    assert result["mode"] == "mock" and result["note"] == MOCK_NOTE and result["trace_id"] is None


def test_mock_mode_is_deterministic():
    question = "What is LangSmith?"
    first, second = run_workflow(question), run_workflow(question)
    assert first["explanation"] == second["explanation"] and first["example"] == second["example"]


def test_small_talk_routes_to_clarify():
    result = run_workflow("hello")
    assert result["steps"] == ["receive", "classify", "clarify", "finalize"]
    assert result["status"] == "needs_clarification" and result["attempts"] == 0 and result["note"] is None


def test_invalid_output_is_retried_once_then_succeeds():
    model = MockChatModel(invalid_times=1)
    result = run_workflow("What is RAG?", model=model)
    assert result["steps"] == ["receive", "classify", "explain", "add_example", "validate",
                               "explain", "add_example", "validate", "finalize"]
    assert result["status"] == "success" and result["attempts"] == 2


def test_failing_model_falls_back_after_bounded_retries():
    model = MockChatModel(fail_times=100)
    result = run_workflow("What is LangChain?", model=model)
    assert result["status"] == "fallback" and result["attempts"] == get_settings().max_attempts == 2
    assert result["steps"][-2:] == ["fallback", "finalize"] and result["steps"].count("explain") == 2
    assert "explanation is missing or too short" in result["validation_errors"]
    assert "LangChain is an open-source framework" in result["explanation"]
    assert "Fallback" in result["note"]


def test_retry_limit_follows_settings(monkeypatch):
    monkeypatch.setenv("MAX_RETRIES", "0")
    result = run_workflow("What is LangChain?", model=MockChatModel(fail_times=100))
    assert result["attempts"] == 1 and result["status"] == "fallback"


def test_route_after_validate():
    assert route_after_validate({"validation_errors": [], "attempts": 1, "max_attempts": 2}) == "finalize"
    assert route_after_validate({"validation_errors": ["x"], "attempts": 1, "max_attempts": 2}) == "explain"
    assert route_after_validate({"validation_errors": ["x"], "attempts": 2, "max_attempts": 2}) == "fallback"


def test_graph_contains_every_node():
    mermaid = workflow_mermaid()
    for node in ["receive", "classify", "clarify", "explain", "add_example", "validate", "fallback", "finalize"]:
        assert node in mermaid


def test_tracing_is_off_without_a_key(monkeypatch):
    monkeypatch.setenv("LANGSMITH_TRACING", "true")
    status = configure_tracing(get_settings())
    assert status["enabled"] is False and "LANGSMITH_API_KEY is missing" in status["reason"]
    assert run_workflow("What is LangGraph?")["status"] == "success"      # still works


def test_tracing_turns_on_with_a_key(monkeypatch):
    monkeypatch.setenv("LANGSMITH_TRACING", "true")
    monkeypatch.setenv("LANGSMITH_API_KEY", "lsv2_test_key_value_123")
    monkeypatch.setenv("LANGSMITH_PROJECT", "unit-test-project")
    status = configure_tracing(get_settings())
    assert status == {"enabled": True, "project": "unit-test-project", "reason": None}
    monkeypatch.setenv("LANGSMITH_TRACING", "false")                      # no network calls from tests
    configure_tracing(get_settings())


def test_logs_never_contain_keys(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-FAKE-not-a-real-key-000")
    record = logging.LogRecord("t", logging.INFO, __file__, 1, "key=%s other=lsv2_abcdefghijk",
                               ("sk-FAKE-not-a-real-key-000",), None)
    SecretRedactingFilter().filter(record)
    assert "FAKE-not-a-real" not in record.getMessage() and "lsv2_abcdefghijk" not in record.getMessage()


def test_reference_notes_ground_known_topics():
    from app.knowledge import reference_notes
    assert "orchestrating stateful" in reference_notes("LangGraph")
    both = reference_notes("LangChain vs LangSmith")
    assert both.startswith("LangChain:") and "LangSmith:" in both
    assert reference_notes("Photosynthesis").startswith("No notes")
