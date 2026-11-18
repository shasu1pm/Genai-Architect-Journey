"""Pydantic models: what the API accepts, what the model must return, and what the API returns."""
from __future__ import annotations

from typing import Annotated, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

QuestionText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=3, max_length=500)]
Mode = Literal["mock", "openai", "ollama"]


# ----------------------------------------------------------------------------- request
class QuestionRequest(BaseModel):
    model_config = ConfigDict(json_schema_extra={
        "examples": [{"question": "What is Agentic AI? Explain with a simple real-world example."}]})

    question: QuestionText = Field(description="An educational question, 3 to 500 characters.")


# ----------------------------------------------------------------------------- model outputs (parsed by LangChain)
class Explanation(BaseModel):
    """Structured output of the explain chain."""
    topic: str = Field(description="The main topic, two to five words")
    explanation: str = Field(description="A beginner-friendly explanation in three to five sentences")
    key_points: list[str] = Field(description="Two to four short key points")


class PracticalExample(BaseModel):
    """Structured output of the example chain."""
    example: str = Field(description="One simple real-world example in two or three sentences")


class LearningAnswer(BaseModel):
    """Structured output of the single-call answer chain used by /ask."""
    topic: str = Field(description="The main topic, two to five words")
    explanation: str = Field(description="A beginner-friendly explanation in three to five sentences")
    example: str = Field(description="One simple real-world example in two or three sentences")


# ----------------------------------------------------------------------------- API responses
class AskResponse(BaseModel):
    question: str
    topic: str
    explanation: str
    example: str
    status: Literal["success"]
    mode: Mode
    note: Optional[str] = Field(None, description="Present in mock mode: the answer is predefined, not generated")


class WorkflowResponse(BaseModel):
    question: str
    topic: str
    question_type: Literal["concept", "comparison", "how_to", "small_talk"]
    explanation: str
    key_points: list[str]
    example: str
    status: Literal["success", "fallback", "needs_clarification"]
    mode: Mode
    note: Optional[str] = None
    steps: list[str] = Field(description="Nodes in the order they ran")
    attempts: int = Field(description="How many times the explain node ran")
    validation_errors: list[str] = Field(description="Problems found by the last validation, if any")
    trace_id: Optional[str] = Field(None, description="LangSmith run id when tracing is enabled")


class LangSmithStatus(BaseModel):
    enabled: bool
    project: Optional[str] = None
    reason: Optional[str] = None


class HealthResponse(BaseModel):
    status: Literal["ok", "degraded"]
    version: str
    llm_provider: str
    model: str
    problem: Optional[str] = None
    langsmith: LangSmithStatus


class ErrorResponse(BaseModel):
    status: Literal["error"] = "error"
    error: str = Field(description="Short machine-readable code, e.g. validation_error")
    detail: str | list[dict] = Field(description="Human-readable explanation; never contains secrets")
