"""LangChain layer — prompt templates, model invocation and structured output.

Each chain is built with LCEL (LangChain Expression Language):

    prompt template  |  chat model  |  output parser

- `ChatPromptTemplate` turns variables (topic, question, style, notes) into chat messages.
- The chat model can be the mock, OpenAI or Ollama — the chain does not change.
- `PydanticOutputParser` checks the reply against a Pydantic schema and returns a typed object;
  a reply that does not match raises an error that the caller can handle.

Two choices make the chains work well even with a small local model:
- the expected output is shown as a short, literal JSON template (small models tend to copy a
  full JSON schema instead of filling it in);
- **grounding notes**: for topics the project knows, short reference notes are added to the
  prompt, so the model writes its own answer from accurate facts instead of guessing.

/ask uses one chain on its own (LangChain alone). /workflow calls the explain and example
chains from LangGraph nodes.
"""
from __future__ import annotations

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from app.knowledge import classify_question, reference_notes
from app.schemas import Explanation, LearningAnswer, PracticalExample

TUTOR = ("You are a patient AI tutor for beginners. Use plain English, short sentences and no jargon "
         "without a definition. Use the background notes for facts and do not contradict them, but write "
         "everything in your own words — never copy the notes word for word. "
         "Never invent facts; if unsure, say so.")

STYLES = {
    "concept": "Explain what it is, why it matters and how it works at a high level.",
    "comparison": "Compare the items side by side: what each is for, how they differ and when to use each.",
    "how_to": "Explain the main steps in order, at a beginner level.",
}

JSON_TEMPLATES = {
    Explanation: '{"topic": "<the topic>", "explanation": "<three to five sentences>", '
                 '"key_points": ["<short point>", "<short point>", "<short point>"]}',
    PracticalExample: '{"example": "<one everyday example in two or three sentences>"}',
    LearningAnswer: '{"topic": "<the topic>", "explanation": "<three to five sentences>", '
                    '"example": "<one everyday example in two or three sentences>"}',
}
_FORMAT = "Reply with JSON only, no other text, in exactly this form:\n{format_instructions}"

_EXPLAIN_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "TASK=explain\n" + TUTOR + "\n{style}\n" + _FORMAT),
    ("human", "Topic: {topic}\nBackground notes: {notes}\nQuestion: {question}"),
])

_EXAMPLE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "TASK=example\n" + TUTOR + "\nGive one simple, realistic, everyday example that makes the "
               "explanation concrete. Describe a situation; do not repeat the definition.\n" + _FORMAT),
    ("human", "Topic: {topic}\nExplanation: {explanation}"),
])

_ANSWER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "TASK=answer\n" + TUTOR + "\nAnswer the question with a short explanation and one real-world "
               "example.\n" + _FORMAT),
    ("human", "Topic: {topic}\nBackground notes: {notes}\nQuestion: {question}"),
])


def _structured(prompt: ChatPromptTemplate, model: BaseChatModel, schema) -> Runnable:
    parser = PydanticOutputParser(pydantic_object=schema)
    return prompt.partial(format_instructions=JSON_TEMPLATES[schema]) | model | parser


def build_explain_chain(model: BaseChatModel) -> Runnable:
    """Inputs: topic, question, style, notes  →  Explanation(topic, explanation, key_points)."""
    return _structured(_EXPLAIN_PROMPT, model, Explanation)


def build_example_chain(model: BaseChatModel) -> Runnable:
    """Inputs: topic, explanation  →  PracticalExample(example)."""
    return _structured(_EXAMPLE_PROMPT, model, PracticalExample)


def build_answer_chain(model: BaseChatModel) -> Runnable:
    """Inputs: topic, question, notes  →  LearningAnswer(topic, explanation, example) in a single model call."""
    return _structured(_ANSWER_PROMPT, model, LearningAnswer)


def answer_question(question: str, model: BaseChatModel, config: dict | None = None) -> LearningAnswer:
    """The /ask path — LangChain on its own: one prompt, one model call, one parsed answer.

    The topic hint comes from the same deterministic classifier the workflow uses.
    Errors (model unavailable, invalid JSON) are raised for the API layer to handle.
    """
    topic = classify_question(question)["topic"]
    return build_answer_chain(model).invoke(
        {"topic": topic, "question": question, "notes": reference_notes(topic)}, config=config)
