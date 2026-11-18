"""Every test runs offline in deterministic mock mode with tracing off, whatever .env contains."""
import pytest


@pytest.fixture(autouse=True)
def offline_mock_mode(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    monkeypatch.setenv("MAX_RETRIES", "1")
    monkeypatch.setenv("LANGSMITH_TRACING", "false")
    monkeypatch.delenv("LANGSMITH_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
