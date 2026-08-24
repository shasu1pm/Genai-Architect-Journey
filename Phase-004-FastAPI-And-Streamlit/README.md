<div align="center">

<img src="../1-Dragon-Motivation-Logo.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="88">

# Phase-004-FastAPI-And-Streamlit — Interfaces and APIs

**Shasu Vathanan - GEN AI - Product Manager**

[![Website](https://img.shields.io/badge/Website-SHASUVATHANAN.COM-FF4A62?style=for-the-badge)](https://shasuvathanan.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-shasuvathanan-031273?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shasuvathanan)

</div>

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**Where the Python from the earlier phases stops being a script and starts being a product.**

Phase-001-Programming-Foundations to Phase-003-Robotic-Process-Automation-(RPA) produced logic that runs in a terminal. Nobody else can use a terminal script. This phase adds the two interfaces that turn that logic into something other people — and other programs — can actually reach: **a web UI with Streamlit**, and **a web API with FastAPI**.

---

## Quick Navigation

| # | Track | What it covers | Go to |
| :-- | :-- | :-- | :-- |
| 1 | **Streamlit** | Turning a Python script into an interactive browser app | [Open](./Streamlit/) |
| 2 | **FirstAPI** | Exposing Python logic as a JSON API other systems can call | [Open](./FirstAPI/) |

---

## What is in this phase

### 🎨 Streamlit — the human interface

| Item | Description |
| :-- | :-- |
| [Introduction to Streamlit](./Streamlit/Introduction%20to%20Streamlit.md) | The full written guide — framework basics, MVP thinking, and a Calculator MVP built step by step |
| [Introduction to Streamlit.pdf](./Streamlit/Introduction%20to%20Streamlit.pdf) | The same guide as a branded, printable document |
| [Streamlit Resources](./Streamlit/Streamlit%20Resources/) | Teaching notebooks and small working apps — BMI calculator, widget tour, full calculator |
| [Streamlit Assignment Details](./Streamlit/Streamlit%20Assignment%20Details/) | **Student Grade App** — the complete build, with screenshots |
| [Streamlit_Basic.py](./Streamlit/Streamlit_Basic.py) | The smallest possible Streamlit app — four lines |

### ⚡ FirstAPI — the machine interface

| Item | Description |
| :-- | :-- |
| [FastAPI Calculator API.pdf](./FirstAPI/FastAPI%20Calculator%20API.pdf) | A complete build guide for the Calculator API — source, endpoints, testing, error handling |
| [calculator.py](./FirstAPI/calculator.py) | The Calculator API — four operations, Pydantic models, guarded division |
| [FirstAPI.py](./FirstAPI/FirstAPI.py) | The first endpoint ever written in this repository |
| [FastAPI App Assignments](./FirstAPI/FastAPI%20App%20Assignments/) | **Basic FastAPI App** — the complete build, with a Postman collection |

---

## Streamlit or FastAPI — which one, and when

Both take the same Python function and make it reachable. They differ in *who* is doing the reaching.

| | **Streamlit** | **FastAPI** |
| :-- | :-- | :-- |
| **Built for** | A person, in a browser | Another program, over HTTP |
| **You write** | Widgets and layout | Endpoints and data models |
| **Returns** | A rendered page | JSON |
| **Run it with** | `streamlit run app.py` | `uvicorn main:app --reload` |
| **Default address** | `http://localhost:8501` | `http://127.0.0.1:8000` |
| **Documentation** | The interface *is* the documentation | Auto-generated at `/docs` |
| **Best for** | Demos, dashboards, internal tools, MVPs | Services, integrations, automation, AI agents |

> [!NOTE]
> These are not competitors. A common production shape is a **FastAPI service holding the logic** with a **Streamlit app calling it** — the API serves every client, and the UI is just one of them.

---

## What this phase demonstrates

- **Both interface models**, built from scratch rather than from a template.
- **Input validation as a first-class concern** — every app here handles empty, non-numeric, and out-of-range input without crashing.
- **Meaningful failure** — HTTP 400 for impossible operations, 422 for malformed data, friendly on-screen messages for people.
- **Evidence of working software** — screenshots for the UI, an importable Postman collection for the API.

---

## Running anything in this phase

Each project folder carries its own `README.md` with exact commands. The general shape is always the same:

```powershell
cd "path\to\the\project"
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Then start it with `streamlit run <file>.py` or `uvicorn <file>:app --reload`.

> [!IMPORTANT]
> Create a fresh virtual environment inside the project you want to run. Virtual environments are machine-specific and are never committed — `requirements.txt` is what makes a project reproducible.

---

## Phase map

| Phase | Focus | Document |
| :-- | :-- | :-- |
| [Phase-001-Programming-Foundations](../Phase-001-Programming-Foundations/) | Python fundamentals — the Student Grade System in a terminal | [📄 PDF](../Phase-001-Programming-Foundations/Student%20Grade%20System.pdf) |
| [Phase-002-GenAI-Python-Toolkit](../Phase-002-GenAI-Python-Toolkit/) | Mandatory Python concepts for Generative AI | [📄 PDF](../Phase-002-GenAI-Python-Toolkit/Mandatory%20Python%20Concepts%20for%20Generative%20AI.pdf) |
| [Phase-003-Robotic-Process-Automation-(RPA)](../Phase-003-Robotic-Process-Automation-%28RPA%29/) | RPA — desktop and browser automation | [📄 PDF](../Phase-003-Robotic-Process-Automation-%28RPA%29/RPA%20-%20Robotic%20Process%20Automation.pdf) |
| **Phase-004-FastAPI-And-Streamlit** | **Interfaces and APIs — Streamlit and FastAPI** | *this phase* |

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

<div align="center">

**Created and Maintained by**

### Shasu Vathanan - GEN AI - Product Manager

[SHASUVATHANAN.COM](https://shasuvathanan.com) &nbsp;•&nbsp; [LinkedIn](https://www.linkedin.com/in/shasuvathanan)

</div>
