---
out: Phase-002-GenAI-Python-Toolkit/GenAI-Python-Toolkit-Explainer.pdf
folder: Phase-002-GenAI-Python-Toolkit
title: GenAI Python Toolkit
subtitle: The 14 Python concepts to master before touching any AI library
fact: Document | Phase explainer
fact: Level | Beginner
fact: Contents | 14 Jupyter notebooks · app.py module example
fact: Tools | Python 3 · VS Code · Jupyter · venv
fact: Source | Lessons based on Python Concepts by Thirumurugan
fact: Folder | Phase-002-GenAI-Python-Toolkit
keywords: Python, notebooks, data types, functions, error handling
---
# What this phase is
lead: Fourteen short, runnable notebooks that cover the Python every GenAI project depends on.
GenAI tools can feel like magic, but the code behind them still runs on ordinary Python: variables, collections, decisions, loops, functions, error handling and files. This phase teaches those foundations with short explanations and code you run, edit and break on purpose.
_note: Lesson content is based on the open-source Python Concepts project by Thirumurugan (github.com/Thirumurugan240/Python_Concepts), credited in the phase README.

# The learning path
| No. | Concept | Why it matters for GenAI |
| :-- | :-- | :-- |
| 01 | What is programming | AI applications follow coded workflows |
| 02 | Python and its uses | Python powers AI models, APIs, data and automation |
| 03 | Python syntax | Clean syntax prevents failures in AI pipelines |
| 04 | Virtual environments | GenAI libraries need specific package versions |
| 05 | Run Python in VS Code | A practical workspace for AI experiments |
| 06 | Operators | Calculations, filtering and decision rules |
| 07 | Data types | Prompts, scores, settings and responses use them |
| 08 | Lists, sets, tuples, dictionaries | AI requests and responses are lists and dictionaries |
| 09 | Control flow | Routing prompts and validating input |
| 10 | Nested if statements | Multi-step validation and access logic |
| 11 | Loops | Processing batches of prompts, files or outputs |
| 12 | Functions | Reusable, testable prompt and model workflows |
| 13 | Error handling | Surviving API, input and runtime failures |
| 14 | File handling | Saving prompts, responses, logs and datasets |

# How to work through it
flow: Set up Python + VS Code > Create a venv > Install ipykernel > Run 01 → 14 in order > Run app.py
```powershell Setup
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install ipykernel
```
Open a notebook, choose **Select Kernel → venv**, read each explanation and run the cells top to bottom. Change the values and predict the output before running again — that is where the learning happens.

# Collections in one picture — an illustrative example
lead: Lesson 08 is the one AI code leans on most, because model requests and responses are lists and dictionaries.
The snippet below is an illustration for this explainer (not a copy of the notebook): a list keeps order, a set removes duplicates, a tuple is fixed, and a dictionary maps keys to values.
```python Illustration — fruits as data
fruits = ["Apple", "Banana", "Mango", "Orange", "Apple"]   # list: ordered, allows repeats
unique = set(fruits)                                       # set: {'Apple', 'Banana', 'Mango', 'Orange'}
point = ("Mango", 3)                                       # tuple: fixed pair
prices = {"Apple": 120, "Banana": 40}                      # dict: key -> value

for fruit in fruits:
    print(fruit)

print(prices["Apple"])                                     # 120
```
> [!TIP] The same shape appears in every chat API
> A chat request is a list of dictionaries such as `{"role": "user", "content": "..."}`. Once lists and dictionaries feel natural, reading AI code becomes much easier.

# The module example — app.py
```python app.py
from modules.addition import add

print(add(1,2))
```
`app.py` shows how reusable code moves into a separate module and is imported. Run it from the phase folder with `python app.py`; the README documents the expected output `3`.
> [!NOTE] Known gap
> The `modules/` package that `app.py` imports is not present in this folder yet, so `python app.py` currently raises `ModuleNotFoundError`. The notebooks are unaffected.

# Troubleshooting
| Problem | Fix |
| :-- | :-- |
| `python` is not recognised | Reinstall Python with **Add Python to PATH**, or try `python3` |
| Notebook cells do not run | Install `ipykernel` and select the `venv` kernel |
| PowerShell blocks activation | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again |
| `ModuleNotFoundError` | Activate the venv and `python -m pip install <package>` |

# Key takeaways
- Lists and dictionaries are the everyday data shapes of AI code.
- Virtual environments keep each project's package versions separate.
- Functions and error handling turn experiments into reusable, reliable code.
- Next: Phase-003-Robotic-Process-Automation-(RPA) — Python that drives other software.
