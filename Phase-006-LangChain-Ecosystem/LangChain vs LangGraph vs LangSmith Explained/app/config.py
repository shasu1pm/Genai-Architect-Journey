"""Configuration and logging.

All settings come from environment variables; a local `.env` file in the project folder is
loaded automatically. `get_settings()` reads them on every call, so tests and the API always
see the current values.

| Variable            | Default                 | Meaning                                         |
|---------------------|-------------------------|-------------------------------------------------|
| LLM_PROVIDER        | mock                    | mock · openai · ollama                          |
| OPENAI_API_KEY      | —                       | required when LLM_PROVIDER=openai               |
| OPENAI_MODEL        | gpt-4.1-mini            | OpenAI chat model                               |
| OLLAMA_MODEL        | qwen2.5:0.5b            | local model served by Ollama                    |
| OLLAMA_BASE_URL     | http://localhost:11434  | Ollama server address                           |
| LLM_TEMPERATURE     | 0.2                     | lower = more focused answers                    |
| MAX_RETRIES         | 1                       | extra attempts when an answer fails validation  |
| LLM_TIMEOUT_SECONDS | 60                      | per-call timeout for real models                |
| LANGSMITH_TRACING   | false                   | true = send traces to LangSmith (needs a key)   |
| LANGSMITH_API_KEY   | —                       | LangSmith key                                   |
| LANGSMITH_PROJECT   | ai-learning-assistant   | LangSmith project that receives the traces      |
| LOG_LEVEL           | INFO                    | DEBUG · INFO · WARNING · ERROR                  |
"""
from __future__ import annotations

import logging
import os
import re
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_DIR / ".env")

PROVIDERS = ("mock", "openai", "ollama")
DEFAULT_PROJECT = "ai-learning-assistant"


def _flag(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def _int(name: str, default: int, low: int, high: int) -> int:
    try:
        return max(low, min(high, int(os.getenv(name, default))))
    except ValueError:
        return default


def _float(name: str, default: float, low: float, high: float) -> float:
    try:
        return max(low, min(high, float(os.getenv(name, default))))
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    llm_provider: str
    openai_model: str
    ollama_model: str
    ollama_base_url: str
    temperature: float
    max_retries: int
    timeout_seconds: float
    log_level: str
    langsmith_tracing: bool
    langsmith_project: str
    has_openai_key: bool
    has_langsmith_key: bool

    @property
    def model_name(self) -> str:
        return {"openai": self.openai_model, "ollama": self.ollama_model}.get(self.llm_provider, "mock-tutor")

    @property
    def max_attempts(self) -> int:
        return 1 + self.max_retries


def get_settings() -> Settings:
    return Settings(
        llm_provider=os.getenv("LLM_PROVIDER", "mock").strip().lower() or "mock",
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        ollama_model=os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b"),
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=_float("LLM_TEMPERATURE", 0.2, 0.0, 1.0),
        max_retries=_int("MAX_RETRIES", 1, 0, 3),
        timeout_seconds=_float("LLM_TIMEOUT_SECONDS", 60.0, 5.0, 300.0),
        log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
        langsmith_tracing=_flag(os.getenv("LANGSMITH_TRACING")),
        langsmith_project=os.getenv("LANGSMITH_PROJECT", DEFAULT_PROJECT),
        has_openai_key=bool(os.getenv("OPENAI_API_KEY")),
        has_langsmith_key=bool(os.getenv("LANGSMITH_API_KEY")),
    )


def provider_problem(settings: Settings) -> str | None:
    """Explain why the configured provider cannot be used, or return None when it can."""
    if settings.llm_provider not in PROVIDERS:
        return f"Unknown LLM_PROVIDER '{settings.llm_provider}'. Use one of: {', '.join(PROVIDERS)}."
    if settings.llm_provider == "openai" and not settings.has_openai_key:
        return "LLM_PROVIDER=openai needs OPENAI_API_KEY in .env (or use LLM_PROVIDER=mock)."
    return None


# ----------------------------------------------------------------------------- safe logging
_SECRET_PATTERNS = [re.compile(r"sk-[A-Za-z0-9_\-]{8,}"), re.compile(r"lsv2_[A-Za-z0-9_\-]{8,}")]


class SecretRedactingFilter(logging.Filter):
    """Masks API keys in every log record — both known patterns and the configured key values."""

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        for name in ("OPENAI_API_KEY", "LANGSMITH_API_KEY"):
            value = os.getenv(name)
            if value and len(value) >= 8:
                message = message.replace(value, "***")
        for pattern in _SECRET_PATTERNS:
            message = pattern.sub("***", message)
        record.msg, record.args = message, ()
        return True


def setup_logging(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("learning_assistant")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
        handler.addFilter(SecretRedactingFilter())
        logger.addHandler(handler)
        logger.propagate = False
    logger.setLevel(getattr(logging, level, logging.INFO))
    return logger
