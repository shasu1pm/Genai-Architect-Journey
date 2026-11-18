"""Built-in learning content and the question classifier.

- `TOPICS` holds short, predefined answers. Mock mode returns them (clearly labelled as mock),
  and the workflow's fallback node uses them when a real model's answer fails validation.
- `classify_question` is plain, deterministic Python: it finds the topic and the kind of
  explanation needed. Keeping it rule-based makes the workflow's routing predictable and testable.
"""
from __future__ import annotations

import re

TOPICS: dict[str, dict] = {
    "Agentic AI": {
        "keywords": ["agentic ai", "agentic", "ai agent", "ai agents", "agents", "agent"],
        "explanation": "Agentic AI refers to AI systems that can plan the steps needed to reach a goal, use tools "
                       "such as search or calculators, check their own progress and continue until the task is done. "
                       "Instead of answering one prompt, an agent works through a multi-step workflow, often asking "
                       "a person to approve important actions.",
        "key_points": ["Works toward a goal, not just a single reply", "Plans steps and chooses tools",
                       "Keeps humans in the loop for important decisions"],
        "example": "An AI travel assistant can research destinations, compare flight and hotel options within your "
                   "budget, and prepare an itinerary that it shows you for approval before anything is booked.",
    },
    "LangChain": {
        "keywords": ["langchain"],
        "explanation": "LangChain is an open-source framework for building applications around language models. "
                       "It gives standard building blocks — chat models, prompt templates, output parsers, tools and "
                       "retrievers — that can be joined into chains, so the same code works with different model providers.",
        "key_points": ["Standard interfaces for many model providers", "Prompt templates and structured output parsing",
                       "Compose steps into reusable chains"],
        "example": "A support team uses a LangChain chain that fills a prompt template with a customer email, sends it "
                   "to a chat model and parses the reply into a category and a draft answer.",
    },
    "LangGraph": {
        "keywords": ["langgraph"],
        "explanation": "LangGraph is a framework for orchestrating stateful, multi-step AI workflows as a graph. "
                       "Each node is a step, edges decide what runs next, and a shared state carries data between steps. "
                       "It supports branching, loops with limits and human review, and it can run any Python code — "
                       "with or without LangChain components inside the nodes.",
        "key_points": ["State shared by every step", "Nodes, edges and conditional routing",
                       "Bounded loops, retries and human-in-the-loop"],
        "example": "A loan pre-check workflow first collects the application, then routes complete applications to an "
                   "automatic summary and incomplete ones to a request for missing documents — the same path every time.",
    },
    "LangSmith": {
        "keywords": ["langsmith"],
        "explanation": "LangSmith is a hosted platform for observing, debugging and evaluating LLM applications. "
                       "It records each run as a trace — inputs, outputs, intermediate steps, latency and token usage — "
                       "and lets you test changes against datasets. It is optional: applications run without it.",
        "key_points": ["Traces every step of a run", "Shows latency, errors and token usage",
                       "Evaluates answers against test datasets"],
        "example": "When a chatbot gives a wrong answer, a developer opens its LangSmith trace, sees that the retriever "
                   "returned an outdated document, fixes the data and re-runs the evaluation dataset to confirm the fix.",
    },
    "FastAPI": {
        "keywords": ["fastapi"],
        "explanation": "FastAPI is a modern Python web framework for building HTTP APIs. You describe requests and "
                       "responses with type hints and Pydantic models; FastAPI validates the data, returns clear errors "
                       "and generates interactive OpenAPI documentation automatically.",
        "key_points": ["Type hints drive validation", "Automatic Swagger UI and OpenAPI schema",
                       "Fast and easy to test"],
        "example": "A mobile app sends a question to a FastAPI endpoint; FastAPI rejects an empty question with a "
                   "clear 422 error and passes valid ones to the AI workflow.",
    },
    "Python": {
        "keywords": ["python"],
        "explanation": "Python is a readable, general-purpose programming language and the most common language for "
                       "AI work. Its large ecosystem — FastAPI, Pydantic, LangChain, LangGraph and pytest among many "
                       "others — lets one person build, serve and test an AI application.",
        "key_points": ["Readable syntax for beginners", "Huge AI and data ecosystem", "Same language from prototype to API"],
        "example": "A student writes a Python script that reads a CSV of exam marks, calculates averages and plots "
                   "the results — then turns the same logic into a small web API.",
    },
    "Retrieval-Augmented Generation": {
        "keywords": ["rag", "retrieval augmented generation", "retrieval-augmented generation", "retrieval"],
        "explanation": "Retrieval-Augmented Generation (RAG) lets a language model answer from your own documents. "
                       "The documents are split into chunks and stored as embeddings; for each question the most "
                       "relevant chunks are retrieved and given to the model as context.",
        "key_points": ["Grounds answers in real documents", "Retrieve first, then generate",
                       "Answer quality depends on retrieval quality"],
        "example": "A company assistant answers 'How many leave days do I have?' by retrieving the HR policy "
                   "section on leave and summarising it, instead of guessing.",
    },
    "Embeddings": {
        "keywords": ["embedding", "embeddings", "vector", "vectors"],
        "explanation": "An embedding is a list of numbers that represents the meaning of a piece of text. Texts with "
                       "similar meaning get similar numbers, so a computer can find related content by comparing vectors.",
        "key_points": ["Text becomes a vector of numbers", "Similar meaning means nearby vectors",
                       "Powers semantic search and RAG"],
        "example": "A recipe app finds 'quick pasta dinner' when you search 'fast spaghetti meal', because both phrases "
                   "have embeddings that are close together.",
    },
    "Prompt engineering": {
        "keywords": ["prompt", "prompts", "prompt engineering", "prompt template"],
        "explanation": "Prompt engineering is the practice of writing clear instructions for a language model: the role, "
                       "the task, the context, the format of the answer and the limits. Small changes in a prompt can "
                       "change the quality of the output a lot.",
        "key_points": ["State the role and the task", "Give context and the output format", "Test and refine"],
        "example": "Asking 'Summarise this email in three bullet points for a busy manager' gives a far more useful "
                   "result than simply asking 'Summarise this'.",
    },
    "Large language models": {
        "keywords": ["llm", "llms", "large language model", "large language models", "language model"],
        "explanation": "A large language model (LLM) is a neural network trained on a very large amount of text to "
                       "predict the next token. That simple objective lets it write, summarise, translate and answer "
                       "questions, but it can also produce confident mistakes, so important answers should be grounded and checked.",
        "key_points": ["Predicts the next token", "General-purpose language skills", "Can be wrong — verify important answers"],
        "example": "A small business owner uses an LLM to draft a product description, then edits the facts and "
                   "prices before publishing it.",
    },
}

GENERIC = {
    "explanation": "{topic} is the subject of your question. In mock mode this assistant only has predefined answers "
                   "for a few core AI topics, so this is a general placeholder: switch LLM_PROVIDER to openai or "
                   "ollama for a real, generated explanation.",
    "key_points": ["Mock mode has predefined answers for core AI topics", "Use a real provider for any topic"],
    "example": "Ask the assistant about Agentic AI, LangChain, LangGraph, LangSmith, RAG, embeddings or FastAPI to "
               "see a complete predefined answer in mock mode.",
}

_SMALL_TALK = re.compile(r"^\s*(hi|hello|hey|thanks|thank you|good (morning|afternoon|evening)|bye|ok|okay)\b[\s!.?]*$", re.I)
_COMPARISON = re.compile(r"\b(vs\.?|versus|difference|differences|compare|comparison|better than)\b", re.I)
_HOW_TO = re.compile(r"^\s*(how|steps|build|create|set up|setup|install|implement)\b", re.I)


def _has(text: str, phrase: str) -> bool:
    return re.search(rf"(?<![\w-]){re.escape(phrase)}(?![\w-])", text, re.I) is not None


def find_topics(text: str) -> list[str]:
    """Known topics mentioned in the text, in the order they appear."""
    found = []
    for name, entry in TOPICS.items():
        positions = [m.start() for k in entry["keywords"]
                     for m in re.finditer(rf"(?<![\w-]){re.escape(k)}(?![\w-])", text, re.I)]
        if positions:
            found.append((min(positions), name))
    return [name for _, name in sorted(found)]


def _guess_topic(question: str) -> str:
    text = re.sub(r"^(what|who|why|how|when|where|which)\s+(is|are|does|do|can|should)\s+", "", question.strip(), flags=re.I)
    text = re.sub(r"^(explain|describe|define|tell me about)\s+", "", text, flags=re.I)
    text = re.split(r"[?.!,]", text)[0].strip()
    words = text.split()[:5]
    return " ".join(words).strip().capitalize() or "General question"


def classify_question(question: str) -> dict:
    """Return {'topic', 'question_type'} — question_type is concept, comparison, how_to or small_talk."""
    if _SMALL_TALK.match(question):
        return {"topic": "Small talk", "question_type": "small_talk"}
    topics = find_topics(question)
    if _COMPARISON.search(question) and len(topics) >= 2:
        return {"topic": " vs ".join(topics[:3]), "question_type": "comparison"}
    topic = topics[0] if topics else _guess_topic(question)
    return {"topic": topic, "question_type": "how_to" if _HOW_TO.match(question) else "concept"}


def predefined_answer(topic: str) -> dict:
    """The built-in answer for a topic (comparisons combine their parts); generic text if unknown."""
    parts = [p.strip() for p in topic.split(" vs ")]
    entries = [TOPICS[p] for p in parts if p in TOPICS]
    if not entries:
        return {"topic": topic, "explanation": GENERIC["explanation"].format(topic=topic),
                "key_points": list(GENERIC["key_points"]), "example": GENERIC["example"]}
    if len(entries) == 1:
        e = entries[0]
        return {"topic": topic, "explanation": e["explanation"], "key_points": list(e["key_points"]),
                "example": e["example"]}
    return {
        "topic": topic,
        "explanation": " ".join(f"{p}: {TOPICS[p]['explanation']}" for p in parts if p in TOPICS),
        "key_points": [f"{p} — {TOPICS[p]['key_points'][0].lower()}" for p in parts if p in TOPICS],
        "example": " ".join(TOPICS[p]["example"] for p in parts if p in TOPICS),
    }


def reference_notes(topic: str) -> str:
    """Short grounding notes for the prompt: the built-in facts for known topics, otherwise a caution.

    Grounding keeps a real model accurate on topics this project knows, while it still writes the
    answer in its own words. Unknown topics are answered from the model's general knowledge.
    """
    parts = [p.strip() for p in topic.split(" vs ")]
    known = [f"{p}: {TOPICS[p]['explanation']}" for p in parts if p in TOPICS]
    if known:
        return " ".join(known)
    return "No notes for this topic — answer from general knowledge and say so if you are unsure."
