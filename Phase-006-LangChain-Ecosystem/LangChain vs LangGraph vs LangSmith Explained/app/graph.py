"""LangGraph layer — a stateful workflow with routing, a bounded retry loop and a fallback.

    START → receive → classify ─┬─ small talk ─────────────────────────→ clarify ──┐
                                └─ learning question → explain → add_example        │
                                                          ↑            ↓            │
                                                          └─ retry ─ validate       │
                                                         (attempts < max)  │ ok     │
                                                                           ↓        ↓
                                              attempts used up → fallback → finalize → END

- State: `LearningState`, a typed dictionary every node reads and updates.
- Nodes: plain Python functions. `explain` and `add_example` call LangChain chains;
  `classify`, `validate`, `fallback` and `finalize` are ordinary code — LangGraph can
  orchestrate any Python, not only LangChain components.
- Conditional edges: `route_after_classify` and `route_after_validate` choose the next node.
- The retry loop is bounded by `max_attempts`, so the workflow always ends.
"""
from __future__ import annotations

import operator
from typing import Annotated, Optional, TypedDict

from langchain_core.exceptions import OutputParserException
from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.graph import END, START, StateGraph
from langsmith import traceable

from app.chains import STYLES, build_example_chain, build_explain_chain
from app.config import Settings, get_settings
from app.knowledge import classify_question, predefined_answer, reference_notes
from app.llm import MOCK_NOTE, MockChatModel, get_chat_model
from app.observability import run_config

FALLBACK_NOTE = "Fallback: a predefined answer, because the model's answer did not pass validation."
MIN_EXPLANATION_WORDS = 12
MIN_EXAMPLE_WORDS = 8


class LearningState(TypedDict, total=False):
    question: str
    topic: str
    question_type: str
    explanation: str
    key_points: list[str]
    example: str
    attempts: int
    max_attempts: int
    validation_errors: list[str]
    errors: Annotated[list[str], operator.add]   # every model error, kept for debugging
    status: str
    steps: Annotated[list[str], operator.add]    # each node appends its name: the path taken


@traceable(name="classify_question")
def _classify(question: str) -> dict:
    return classify_question(question)


def _error_text(exc: Exception) -> str:
    if isinstance(exc, OutputParserException):
        return "The model's reply did not match the expected JSON schema."
    return f"The model call failed ({type(exc).__name__})."


def build_workflow(model: BaseChatModel, max_attempts: int = 2):
    """Compile the workflow for one chat model."""
    explain_chain = build_explain_chain(model)
    example_chain = build_example_chain(model)

    def receive(state: LearningState) -> dict:
        return {"question": state["question"].strip(), "attempts": 0, "max_attempts": max_attempts,
                "validation_errors": [], "steps": ["receive"]}

    def classify(state: LearningState) -> dict:
        return {**_classify(state["question"]), "steps": ["classify"]}

    def clarify(state: LearningState) -> dict:
        return {"explanation": "Hello! I explain AI and software topics. Ask a learning question, for example: "
                               "'What is Agentic AI? Explain with a simple real-world example.'",
                "key_points": [], "example": "", "status": "needs_clarification", "steps": ["clarify"]}

    def explain(state: LearningState) -> dict:
        update: dict = {"attempts": state["attempts"] + 1, "steps": ["explain"]}
        try:
            result = explain_chain.invoke({"topic": state["topic"], "question": state["question"],
                                           "style": STYLES[state["question_type"]],
                                           "notes": reference_notes(state["topic"])})
            update.update(explanation=result.explanation.strip(),
                          key_points=[p.strip() for p in result.key_points if p.strip()])
        except Exception as exc:  # model unavailable or invalid output: record it, validation decides
            update.update(explanation="", key_points=[], errors=[_error_text(exc)])
        return update

    def add_example(state: LearningState) -> dict:
        if not state.get("explanation"):
            return {"example": "", "steps": ["add_example"]}
        try:
            result = example_chain.invoke({"topic": state["topic"], "explanation": state["explanation"]})
            return {"example": result.example.strip(), "steps": ["add_example"]}
        except Exception as exc:
            return {"example": "", "errors": [_error_text(exc)], "steps": ["add_example"]}

    def validate(state: LearningState) -> dict:
        problems = []
        if len(state.get("explanation", "").split()) < MIN_EXPLANATION_WORDS:
            problems.append("explanation is missing or too short")
        if not state.get("key_points"):
            problems.append("key points are missing")
        if len(state.get("example", "").split()) < MIN_EXAMPLE_WORDS:
            problems.append("example is missing or too short")
        return {"validation_errors": problems, "steps": ["validate"]}

    def fallback(state: LearningState) -> dict:
        answer = predefined_answer(state["topic"])
        return {"explanation": answer["explanation"], "key_points": answer["key_points"],
                "example": answer["example"], "status": "fallback", "steps": ["fallback"]}

    def finalize(state: LearningState) -> dict:
        return {"status": state.get("status") or "success", "steps": ["finalize"]}

    graph = StateGraph(LearningState)
    for name, fn in [("receive", receive), ("classify", classify), ("clarify", clarify), ("explain", explain),
                     ("add_example", add_example), ("validate", validate), ("fallback", fallback),
                     ("finalize", finalize)]:
        graph.add_node(name, fn)

    graph.add_edge(START, "receive")
    graph.add_edge("receive", "classify")
    graph.add_conditional_edges("classify", route_after_classify, {"clarify": "clarify", "explain": "explain"})
    graph.add_edge("clarify", "finalize")
    graph.add_edge("explain", "add_example")
    graph.add_edge("add_example", "validate")
    graph.add_conditional_edges("validate", route_after_validate,
                                {"finalize": "finalize", "explain": "explain", "fallback": "fallback"})
    graph.add_edge("fallback", "finalize")
    graph.add_edge("finalize", END)
    return graph.compile(name="learning_workflow")


def route_after_classify(state: LearningState) -> str:
    return "clarify" if state["question_type"] == "small_talk" else "explain"


def route_after_validate(state: LearningState) -> str:
    if not state["validation_errors"]:
        return "finalize"
    if state["attempts"] < state["max_attempts"]:
        return "explain"          # bounded retry
    return "fallback"


def run_workflow(question: str, settings: Optional[Settings] = None, model: Optional[BaseChatModel] = None,
                 tracing_enabled: bool = False) -> dict:
    """Run the workflow and return a dict that matches schemas.WorkflowResponse."""
    settings = settings or get_settings()
    model = model or get_chat_model(settings)
    workflow = build_workflow(model, settings.max_attempts)
    config, run_id = run_config("learning-workflow", ["langgraph", "workflow"],
                                {"provider": settings.llm_provider, "model": settings.model_name})
    state = workflow.invoke({"question": question, "steps": [], "errors": []}, config=config)

    notes = []
    if settings.llm_provider == "mock" and state["status"] != "needs_clarification":
        notes.append(MOCK_NOTE)
    if state["status"] == "fallback":
        notes.append(FALLBACK_NOTE)
    return {
        "question": state["question"], "topic": state["topic"], "question_type": state["question_type"],
        "explanation": state["explanation"], "key_points": state.get("key_points", []),
        "example": state.get("example", ""), "status": state["status"], "mode": settings.llm_provider,
        "note": " ".join(notes) or None, "steps": state["steps"], "attempts": state.get("attempts", 0),
        "validation_errors": state.get("validation_errors", []),
        "trace_id": run_id if tracing_enabled else None,
    }


def workflow_mermaid() -> str:
    """The compiled graph as Mermaid text (no model call is made)."""
    return build_workflow(MockChatModel()).get_graph().draw_mermaid()
