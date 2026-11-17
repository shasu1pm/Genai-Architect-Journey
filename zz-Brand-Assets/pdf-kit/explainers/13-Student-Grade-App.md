---
out: Phase-004-FastAPI-And-Streamlit/Streamlit/Streamlit Assignment Details/Student-Grade-App-Explainer.pdf
folder: Phase-004-FastAPI-And-Streamlit
title: Student Grade App
subtitle: A Streamlit web app that turns a mark from 0 to 100 into a letter grade — with friendly validation
fact: Document | Sub-project explainer
fact: Level | Beginner
fact: Script | grade_app.py (single file)
fact: Tools | Python 3.9+ · Streamlit
fact: Evidence | screenshots/ — marks 90, 85 and 59
fact: Folder | …/Streamlit/Streamlit Assignment Details
keywords: Streamlit, grade app, validation
---
# What it is
lead: The Phase-001 grading logic, rebuilt as a web app anyone can use in a browser.
The Student Grade App accepts whole-number and decimal marks from 0 to 100, applies exact inclusive grade boundaries, and shows both the entered mark and the grade. Empty, non-numeric and out-of-range input each get a friendly message instead of an error.

# From terminal program to web app
flow: Phase-001 terminal program > Same grading rule > Streamlit input + button > Validated result in the browser
The rule does not change between Phase-001-Programming-Foundations and this app — only the interface does. That is the point of separating logic from input and output.

# Grading scale
| Mark | Grade |
| :-- | :-- |
| 90–100 | **A** |
| 80 to below 90 | **B** |
| 70 to below 80 | **C** |
| 60 to below 70 | **D** |
| Below 60 | **E** |
> [!NOTE] Boundaries are inclusive
> Exactly 90 is an A, exactly 80 a B, exactly 70 a C and exactly 60 a D.

# Invalid-input handling
| Input | What the app shows |
| :-- | :-- |
| Empty field | A prompt to enter a mark — no calculation attempted |
| Text or other non-numeric input | A friendly validation message |
| Below 0 or above 100 | A range warning |
None of these paths crashes the app; every one ends in a readable message and the user can try again.

# Run it
```powershell Setup and run
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run grade_app.py
```
The app opens at `http://localhost:8501`. Press `Ctrl + C` to stop it.

# Test marks that cover every band
| Mark | Expected grade |
| :-- | :-- |
| 100 · 90 | A |
| 89 · 80 | B |
| 70 | C |
| 60 | D |
| 59 · 0 | E |
The `screenshots/` folder shows the running app for marks 90 (A), 85 (B) and 59 (E).

# Key takeaways
- Reuse logic across interfaces: terminal today, web tomorrow, API next.
- Test the boundaries, not just the middle of each band.
- Validation messages are part of the user experience, not an afterthought.
