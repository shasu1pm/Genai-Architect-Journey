"""Evaluate the workflow on a small dataset — locally, and optionally in LangSmith.

    python examples/evaluate.py              local evaluation (works in mock mode, no key needed)
    python examples/evaluate.py --langsmith  also upload the dataset and run a LangSmith experiment
                                             (needs LANGSMITH_API_KEY and internet access)

Each evaluator is a small Python function that scores one answer. The same functions are used
locally and in LangSmith, where every experiment is stored and can be compared over time.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import get_settings  # noqa: E402
from app.graph import run_workflow  # noqa: E402

DATASET_NAME = "ai-learning-assistant-basics"
DATASET = [
    {"question": "What is Agentic AI? Explain with a simple real-world example.", "topic": "Agentic AI", "status": "success"},
    {"question": "What is LangGraph?", "topic": "LangGraph", "status": "success"},
    {"question": "LangChain vs LangSmith: what is the difference?", "topic": "LangChain vs LangSmith", "status": "success"},
    {"question": "How do I build an API with FastAPI?", "topic": "FastAPI", "status": "success"},
    {"question": "Hello!", "topic": "Small talk", "status": "needs_clarification"},
]


# ----------------------------------------------------------------------------- evaluators
def topic_matches(outputs: dict, reference_outputs: dict) -> bool:
    return outputs["topic"] == reference_outputs["topic"]


def status_matches(outputs: dict, reference_outputs: dict) -> bool:
    return outputs["status"] == reference_outputs["status"]


def has_example(outputs: dict, reference_outputs: dict) -> bool:
    if reference_outputs["status"] != "success":
        return True                      # clarifications have no example by design
    return len(outputs["example"].split()) >= 8


EVALUATORS = [topic_matches, status_matches, has_example]


def target(inputs: dict) -> dict:
    return run_workflow(inputs["question"])


def evaluate_locally() -> None:
    print(f"Local evaluation — provider: {get_settings().llm_provider}\n")
    totals = {e.__name__: 0 for e in EVALUATORS}
    for row in DATASET:
        outputs = target({"question": row["question"]})
        scores = {e.__name__: e(outputs, row) for e in EVALUATORS}
        for name, ok in scores.items():
            totals[name] += ok
        print(f"{'PASS' if all(scores.values()) else 'FAIL'}  {row['question'][:55]:<55}  "
              + "  ".join(f"{k}={'y' if v else 'n'}" for k, v in scores.items()))
    print("\nScore: " + "  ".join(f"{k} {v}/{len(DATASET)}" for k, v in totals.items()))


def evaluate_in_langsmith() -> None:
    """Upload the dataset (once) and run an experiment. Requires a LangSmith account and key."""
    if not get_settings().has_langsmith_key:
        sys.exit("LANGSMITH_API_KEY is not set — the hosted LangSmith experiment was skipped.")
    from langsmith import Client
    client = Client()
    if not client.has_dataset(dataset_name=DATASET_NAME):
        dataset = client.create_dataset(DATASET_NAME, description="AI Learning Assistant — basic questions")
        client.create_examples(dataset_id=dataset.id,
                               examples=[{"inputs": {"question": r["question"]},
                                          "outputs": {"topic": r["topic"], "status": r["status"]}} for r in DATASET])
    results = client.evaluate(target, data=DATASET_NAME, evaluators=EVALUATORS,
                              experiment_prefix=f"learning-assistant-{get_settings().llm_provider}")
    print("LangSmith experiment created:", results.experiment_name)


if __name__ == "__main__":
    evaluate_locally()
    if "--langsmith" in sys.argv:
        evaluate_in_langsmith()
