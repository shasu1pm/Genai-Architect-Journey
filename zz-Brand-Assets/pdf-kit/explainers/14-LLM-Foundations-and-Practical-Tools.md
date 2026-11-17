---
out: Phase-005-LLM-Foundations-and-Practical-Tools/LLM-Foundations-and-Practical-Tools-Explainer.pdf
folder: Phase-005-LLM-Foundations-and-Practical-Tools
title: LLM Foundations and Practical Tools
subtitle: From what the three letters in LLM mean, to a model running locally on your own laptop
short: LLM Foundations
fact: Document | Phase explainer (overview of the 3-part guide)
fact: Level | Beginner to intermediate
fact: Contents | 10 topics · 3-part PDF guide · 102-slide deck · opensource.py
fact: Tools | Hugging Face · Ollama · OpenAI platform
fact: Folder | Phase-005-LLM-Foundations-and-Practical-Tools
keywords: LLM, open source, closed source, benchmarks, Hugging Face, Ollama
---
# What this phase is
lead: The earlier phases built the Python, the automation and the interfaces. This phase adds the model itself.
Ten topics explain what an LLM is, how it works, how open and closed models differ, what access costs, how models are measured, and the two practical ways to run one on your own machine. The full guide is split into three PDFs of up to 15 pages each, with a matching 102-slide deck.

# Four themes, ten topics
| Theme | Topics | The question it answers |
| :-- | :-- | :-- |
| **Foundations** | 01 LLM and its types · 02 Open-source vs cloud LLM | What is an LLM, and what are the two families? |
| **The closed path** | 03 Closed-source LLM · 04 Buying API keys · 05 Benchmarks | How do I buy access, and how do I choose a model? |
| **The toolkit** | 06 Essential AI tools · 07 Hugging Face Spaces | What do I install, and what is already free? |
| **The open path** | 08 Hugging Face models · 09 Ollama · 10 Hands-on practice | How do I run a model myself? |

# Foundations in one page
- **Large + Language + Model:** trained on very large text data, works in human language, and predicts what comes next.
- **Tokens** are the unit you are billed on; **embeddings** turn meaning into numbers; **attention** relates each word to the others.
- The family: **LLM** (text), **LMM** (text, image, audio, video), **SLM** (small, efficient) and **VLM** (vision + language).

# Open or closed — with familiar companies
| | Open-source LLM | Closed / cloud LLM |
| :-- | :-- | :-- |
| Access | Model files downloaded to you | Usage rights through the provider's API |
| Cost | No API cost once downloaded | Pay per million input and output tokens |
| Privacy | Data stays on your machine | Requests travel to the provider |
| Familiar examples | Meta's Llama family, run through Ollama | Google's Gemini, OpenAI's GPT models |
_note: Company examples illustrate the two families; check each provider's current licence and model line-up before relying on them.

# The closed path — access with discipline
flow: Choose one provider > Add $10 credit > Turn auto top-up OFF > Create the secret key > Keep it out of code and screenshots
> [!TIP] The two rules that protect your wallet
> Buy **one** key while learning — compatibility beats variety — and keep **auto top-up off**. Benchmarks such as SWE-bench, Humanity's Last Exam and GDPval then help you match a model to the job instead of picking the most famous name.

# The toolkit — spend nothing while learning
| Category | What it is for | Examples |
| :-- | :-- | :-- |
| Gen AI chat tools | Your daily assistant | ChatGPT · Gemini · Claude · Qwen · DeepSeek |
| AI code editors | Where you build | Cursor · GitHub Copilot · Replit |
| Agentic tools | Autonomous task execution | Covered in a later phase |
**Hugging Face Spaces** are free, community-built apps running in the browser — OCR and image upscaling are two high-value examples.

# The open path — run a model yourself
| | Method 1 · Hugging Face + Python (Topic 08) | Method 2 · Ollama (Topic 09) |
| :-- | :-- | :-- |
| Effort | Project setup, login, download, run script | Install, `ollama pull`, `ollama run` |
| Best for | Learning how loading and generation work | Everyday local use |
| In this folder | `opensource.py` | Commands in the guide |
```text Topic 10 — hands-on task
ollama --version
ollama pull qwen2.5:0.5b      # about 400 MB
ollama run qwen2.5:0.5b       # give it an input, capture the output
```
> [!NOTE] Respect your machine
> Most open models are 2–10 GB, and 16 GB+ RAM with a good GPU is the comfortable baseline. Start small — Qwen2.5 0.5B is chosen for exactly that reason.

# Where to read more
| Document | Topics |
| :-- | :-- |
| LLM-Foundations-and-Practical-Tools-Part-1.pdf | 01–03 |
| LLM-Foundations-and-Practical-Tools-Part-2.pdf | 04–07 |
| LLM-Foundations-and-Practical-Tools-Part-3.pdf | 08–10 |
| LLM-Foundations-and-Practical-Tools.pptx | All ten, as 102 slides |

# Key takeaways
- Know the two families; choose open for control and privacy, closed for frontier capability.
- Buy access responsibly and judge models with benchmarks, not hype.
- Running a small model locally is the moment the concepts become real.
- Next: Transformer-Explorer-Guide (how the model works inside) and Phase-006-LangChain-Ecosystem.
