# Mandatory Python Concepts for Generative AI

## Introduction

This beginner-friendly project teaches the Python foundations needed before working with Generative AI (GenAI). The lessons use short explanations, relatable examples, and runnable Jupyter notebooks. Follow them in order, practise the code, and build the confidence to read, write, and debug Python used in AI projects.

> **Created by:** [Thirumurugan](https://github.com/Thirumurugan240)  
> **Source:** [Python Concepts](https://github.com/Thirumurugan240/Python_Concepts)

## Purpose

GenAI tools may feel like magic, but the code behind them still depends on solid Python basics. This project helps learners aged 15–25 build those basics without unnecessary jargon.

## Learning Objectives

By the end of this project, you will be able to:

- understand and run basic Python programs;
- use variables, data types, operators, and collections;
- control program behaviour with conditions and loops;
- organise reusable logic with functions and modules;
- handle errors and work with files safely; and
- prepare a clean Python environment for future GenAI libraries and projects.

## Project Overview

| Item | Details |
|---|---|
| Level | Beginner |
| Format | 14 Jupyter notebooks and one Python module example |
| Learning style | Read → run → edit → experiment |
| Recommended order | Complete lessons `01` through `14` |
| Final practice | Run `app.py` to see a custom module in action |
| Core dependency | Python 3 |

## Quick Navigation

- [Environment Setup](#environment-setup)
- [Installed Packages](#installed-packages)
- [Tools](#tools)
- [How to Use This Project](#how-to-use-this-project)
- [Learning Path](#learning-path)
- [Project Structure](#project-structure)
- [Module Example](#module-example)
- [Troubleshooting](#troubleshooting)
- [References](#references)
- [Contributing](#contributing)

## Environment Setup

Install and configure the tools in this order.

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/). On Windows, select **Add Python to PATH** during installation.

Verify the installation:

```bash
python --version
pip --version
```

If `python` is not recognised on macOS or Linux, try `python3`.

### 2. Install Visual Studio Code

Download and install [Visual Studio Code](https://code.visualstudio.com/).

### 3. Install VS Code Extensions

Open the **Extensions** panel in VS Code and install the following extensions by Microsoft:

| Tool | When to install | Why it is needed | Where it is used |
|---|---|---|---|
| Python | After installing VS Code | Runs, formats, and debugs Python | `.py` files and Python environments |
| Jupyter | After the Python extension | Opens and runs notebook cells | All `.ipynb` lessons |

### 4. Download the Project

Clone the source repository:

```bash
git clone https://github.com/Thirumurugan240/Python_Concepts.git
cd Python_Concepts
```

You can also download the repository as a ZIP from GitHub and extract it.

### 5. Create a Virtual Environment

From the project folder, create an isolated environment:

```bash
python -m venv venv
```

Activate it:

| Platform | Command |
|---|---|
| Windows PowerShell | `.\venv\Scripts\Activate.ps1` |
| Windows Command Prompt | `venv\Scripts\activate.bat` |
| macOS or Linux | `source venv/bin/activate` |

When finished, leave the environment with:

```bash
deactivate
```

### 6. Install Notebook Support

With the virtual environment active, run:

```bash
python -m pip install --upgrade pip
python -m pip install ipykernel
```

In VS Code, open a notebook, click **Select Kernel**, and choose the `venv` Python environment.

## Installed Packages

The lesson code mainly uses built-in Python features. No package is required for the core examples besides notebook support.

| Package | When to install | Why it is needed | Where it is used | Installation command |
|---|---|---|---|---|
| `ipykernel` | During initial setup | Runs notebook cells with the selected environment | All `.ipynb` notebooks | `python -m pip install ipykernel` |
| `requests` | Optional, while learning virtual environments | Demonstrates installing a third-party library | Installation example in Lesson 04 | `python -m pip install requests` |

> **Note:** `venv` is included with Python and normally does not need a separate installation.

## Tools

| Tool | Purpose | Used for |
|---|---|---|
| Python 3 | Programming language and runtime | Every lesson and `app.py` |
| `pip` | Python package manager | Installing `ipykernel` and optional libraries |
| `venv` | Environment isolation | Keeping project packages separate |
| Visual Studio Code | Code editor | Editing and running project files |
| Python extension | Python support in VS Code | Running and debugging `.py` files |
| Jupyter extension | Notebook support in VS Code | Running `.ipynb` lessons |
| Git | Version control | Cloning and tracking the project |

## How to Use This Project

1. Complete the [Environment Setup](#environment-setup).
2. Open this project folder in VS Code.
3. Start with `01_What_is_Programming.ipynb`.
4. Read each explanation, then run its code cells from top to bottom.
5. Change the example values and predict the output before running again.
6. Complete the notebooks in numerical order.
7. Run `python app.py` after Lesson 12 to explore a reusable module.
8. Build a mini project using functions, error handling, and file handling.

> **Learning tip:** Do not only watch the code run. Break it, fix it, and remix it—that is where the real learning happens.

## Learning Path

| No. | Concept | What you will learn | Why it matters for GenAI |
|---:|---|---|---|
| 01 | [What Is Programming](01_What_is_Programming.ipynb) | Instructions, programs, and programming languages | Helps you understand how AI applications follow coded workflows |
| 02 | [Python and Its Uses](02_Python_and_Uses.ipynb) | Why Python is popular and where it is used | Python is widely used for AI models, APIs, data, and automation |
| 03 | [Python Syntax](03_Python_Syntax.ipynb) | `print()`, comments, indentation, and case sensitivity | Clean syntax prevents failures in AI pipelines |
| 04 | [Python Virtual Environment](04_Python_Virtual_Environment.ipynb) | Creating, activating, and managing isolated environments | GenAI libraries often need specific package versions |
| 05 | [Run Python in VS Code](05_How_to_Run_Python_in_VSCode.ipynb) | Running `.py` files and Jupyter notebooks | Creates a practical workspace for AI experiments |
| 06 | [Python Operators](06_Python_Operators.ipynb) | Arithmetic, comparison, logical, and assignment operators | Used in calculations, filtering, and decision rules |
| 07 | [Python Data Types](07_Python_Data_Types.ipynb) | Variables, integers, floats, strings, booleans, and conversion | Prompts, scores, settings, and model responses use these types |
| 08 | [Lists, Sets, Tuples, and Dictionaries](08_Lists_Sets_Tuples_Dictionary.ipynb) | Storing, accessing, and organising collections | AI requests and responses commonly use lists and dictionaries |
| 09 | [Python Control Flow](09_Python_Control_Flow.ipynb) | `if`, `elif`, and `else` decisions | Routes prompts, validates input, and controls model behaviour |
| 10 | [Nested If Statements](10_Nested_If_Statements.ipynb) | Decisions inside other decisions | Supports multi-step validation and access logic |
| 11 | [Python Loops](11_Python_Loops_Explained.ipynb) | `for`, `while`, `range()`, `break`, and `continue` | Processes batches of prompts, files, or model outputs |
| 12 | [Python Functions](12_Python_Function.ipynb) | Parameters, return values, and reusable logic | Keeps prompt and model workflows reusable and testable |
| 13 | [Error Handling](13_Error_Handling.ipynb) | `try`, `except`, `else`, and `finally` | Handles API, input, and runtime failures without crashing |
| 14 | [Python File Handling](14_Python_File_Handling.ipynb) | Creating, reading, writing, and appending files | Saves prompts, responses, logs, and datasets |

## Project Structure

| Path | Type | Purpose |
|---|---|---|
| `01_...ipynb` to `14_...ipynb` | Jupyter notebooks | Ordered learning content and runnable examples |
| `app.py` | Python script | Imports and runs the custom `add()` function |
| `modules/__init__.py` | Package marker | Makes `modules` a Python package |
| `modules/addition.py` | Python module | Defines the reusable `add(a, b)` function |
| `README.md` | Documentation | Setup, navigation, and learning guide |

## Module Example

The project includes a tiny example of splitting reusable code into another file:

```python
from modules.addition import add

print(add(1, 2))
```

Run it from the project root:

```bash
python app.py
```

Expected output:

```text
3
```

This same pattern scales to GenAI projects, where prompt templates, model calls, data processing, and utility functions are often kept in separate modules.

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| `python` is not recognised | Python is missing from `PATH` | Reinstall Python with **Add Python to PATH**, or try `python3` |
| Notebook cells do not run | No notebook kernel is selected | Install `ipykernel` and select the `venv` kernel |
| PowerShell blocks activation | Script execution policy restriction | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again |
| `ModuleNotFoundError` appears | Package is missing from the active environment | Activate `venv` and install the named package with `python -m pip install <package>` |
| `modules` cannot be imported | `app.py` was run from another folder | Open a terminal at the project root and run `python app.py` |

## References

| Resource | Link |
|---|---|
| Python documentation | [docs.python.org](https://docs.python.org/3/) |
| Python downloads | [python.org/downloads](https://www.python.org/downloads/) |
| VS Code Python guide | [code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial) |
| Jupyter in VS Code | [code.visualstudio.com/docs/datascience/jupyter-notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) |
| Source repository | [github.com/Thirumurugan240/Python_Concepts](https://github.com/Thirumurugan240/Python_Concepts) |

---

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

**Maintained by:**

**Shasu Vathanan** **•** **Gen AI Product Manager**
