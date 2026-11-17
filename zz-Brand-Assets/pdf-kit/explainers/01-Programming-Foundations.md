---
out: Phase-001-Programming-Foundations/Programming-Foundations-Explainer.pdf
folder: Phase-001-Programming-Foundations
title: Programming Foundations
subtitle: Python fundamentals, proven with a Student Grade System that never crashes on bad input
fact: Document | Phase explainer
fact: Level | Beginner
fact: Project | Student Grade System — grade_system.py
fact: Tools | Python 3 · terminal
fact: Folder | Phase-001-Programming-Foundations
keywords: Python, input validation, functions, grade system
---
# What this phase is
lead: The first working program of the journey: read a mark, validate it, and print a letter grade.
Phase-001-Programming-Foundations is where the journey starts writing real Python. The project is small on purpose — a terminal program that converts a mark from 0 to 100 into a letter grade — because every habit it needs (functions, conditions, type conversion and input validation) reappears in every later phase, from Streamlit apps to LLM pipelines.

# Why it matters
- Every AI application still begins with plain Python: reading input, deciding, and returning a result.
- **Validating input before using it** is the single habit that separates a demo from a dependable tool.
- The same grading logic is rebuilt as a web app in Phase-004-FastAPI-And-Streamlit — the logic stays, the interface changes.

# What is in this folder
| File | What it is |
| :-- | :-- |
| `grade_system.py` | The complete program — `calculate_grade()` and `main()` |
| `Student Grade System.pdf` | The project document |
| `Screenshot of the terminal …png` | Evidence of the program running with several marks |
| `README.md` | Run command, grade scale and example runs |

# How it works
flow: Read the mark > Convert to a number > Check 0–100 > Pick the grade > Print the result
`main()` reads the mark as text, converts it with `float()`, and rejects anything that is not a finite number between 0 and 100. Only a valid mark reaches `calculate_grade()`, which checks the bands from the top down so the first matching band wins.
```python grade_system.py — the grading rule
def calculate_grade(mark: float) -> str:
    """Return the letter grade for a validated mark."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"
```
| Mark | Grade |
| :-- | :-- |
| 90–100 | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| Below 60 | E |

# Run it
```powershell Terminal
python grade_system.py
```
```text Expected output
Enter your mark (0-100): 95
Mark: 95 -> Grade: A

Enter your mark (0-100): 85
Mark: 85 -> Grade: B

Enter your mark (0-100): 59
Mark: 59 -> Grade: E
```
> [!NOTE] Invalid input never crashes the program
> Text such as `abc` produces a request to enter a number. Values outside 0–100 — including non-finite values such as `nan` — produce a clear range error. The `math.isfinite()` check is what catches `nan` and `inf`, which `float()` would otherwise accept.

# Key takeaways
- Separate the **rule** (`calculate_grade`) from the **input/output** (`main`) — the rule can then be reused anywhere.
- Convert and validate input first; only clean data reaches the logic.
- Ordered `if` checks from the highest band down keep boundary handling simple and correct.
- Next: Phase-002-GenAI-Python-Toolkit — the full set of Python concepts needed before any AI library.
