"""LangSmith observability — optional.

LangChain and LangGraph send traces to LangSmith by themselves when these variables are set:
LANGSMITH_TRACING=true, LANGSMITH_API_KEY=<key>, LANGSMITH_PROJECT=<project>.

This module only decides whether tracing can be on:
- tracing requested and a key present  → on;
- tracing requested but no key         → switched off, with a clear reason (the app keeps working);
- tracing not requested                → off.

Every run gets its own run id. When tracing is on, the API returns it as `trace_id`, so a
run can be found in LangSmith. Hosted LangSmith needs an account, an API key, internet access
and is subject to the service's plan limits.
"""
from __future__ import annotations

import os
import uuid

from app.config import Settings


def configure_tracing(settings: Settings) -> dict:
    """Apply the tracing decision to the environment and describe it (never includes the key)."""
    if settings.langsmith_tracing and settings.has_langsmith_key:
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_PROJECT"] = settings.langsmith_project
        return {"enabled": True, "project": settings.langsmith_project, "reason": None}
    if settings.langsmith_tracing:
        os.environ["LANGSMITH_TRACING"] = "false"
        return {"enabled": False, "project": None,
                "reason": "LANGSMITH_TRACING is true but LANGSMITH_API_KEY is missing — tracing is off."}
    return {"enabled": False, "project": None, "reason": "LANGSMITH_TRACING is not enabled."}


def run_config(run_name: str, tags: list[str], metadata: dict) -> tuple[dict, str]:
    """A LangChain/LangGraph run config with a fixed run id, so the trace can be looked up later."""
    run_id = uuid.uuid4()
    config = {"run_name": run_name, "run_id": run_id, "tags": tags, "metadata": metadata}
    return config, str(run_id)
