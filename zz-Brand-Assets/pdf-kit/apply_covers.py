"""Give every rebuilt PDF the same brand cover as the explainers.

The old covers held only a title, a subtitle and a facts table, so those exact values are
carried over below and the page is redrawn with `brand_pdf.draw_cover`. Designed covers that
carry their own content (a topic list, a product screenshot) are kept, and a brand cover is
inserted in front of them instead.

Run:  python zz-Brand-Assets/pdf-kit/apply_covers.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import fitz

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rebrand_existing import P3, P4, REPO, _cover_pdf, _save  # noqa: E402

P3S = "…/PyAutoGUI Automation"
P3P = "…/Playwright Automation"

COVERS = [
    ("Phase-001-Programming-Foundations/Student Grade System.pdf", "Phase-001-Programming-Foundations",
     "Student Grade System", "Python fundamentals, validated end to end",
     [("Phase", "Phase-001 - Python Fundamentals"), ("What it is", "A terminal program that turns a mark into a letter grade"),
      ("Level", "Beginner"), ("Tools", "Python 3 · Windows PowerShell"), ("Single file", "grade_system.py"),
      ("Folder", "Phase-001-Programming-Foundations")]),
    ("Phase-002-GenAI-Python-Toolkit/Mandatory Python Concepts for Generative AI.pdf", "Phase-002-GenAI-Python-Toolkit",
     "Python for Generative AI", "The 14 concepts to master before touching an AI library",
     [("Phase", "Phase-002 - Python Foundations"), ("Format", "14 Jupyter notebooks and one module example"),
      ("Level", "Beginner"), ("Learning style", "Read - run - edit - experiment"), ("Core dependency", "Python 3"),
      ("Folder", "Phase-002-GenAI-Python-Toolkit")]),
    (f"{P3}/RPA - Robotic Process Automation.pdf", P3, "Robotic Process Automation",
     "Driving the desktop and the browser from Python",
     [("Phase", "Phase-003 - Automation"), ("Tracks", "PyAutoGUI (desktop) · Playwright (browser)"),
      ("Projects", "Six - two fundamentals sets and four complete bots"), ("Level", "Intermediate"),
      ("Platform", "Windows 10 or 11 · Python 3.10+"), ("Folder", P3)]),
    (f"{P3}/PyAutoGUI Automation/PyAutoGUI Automation.pdf", P3, "PyAutoGUI Automation",
     "Desktop RPA - driving the mouse, keyboard, and screen",
     [("Track", "PyAutoGUI - desktop automation"), ("Contents", "Four fundamentals scripts and two complete bots"),
      ("Level", "Beginner to Intermediate"), ("Platform", "Windows 10 or 11 · Python 3.10+"), ("Folder", P3S)]),
    (f"{P3}/PyAutoGUI Automation/Assignment-1-PyAutoGUI_Weather_Data/Bengaluru Weather Bot.pdf", P3,
     "Bengaluru Weather Bot", "Chrome to Notepad, without an API",
     [("Track", "PyAutoGUI - desktop automation"), ("What it does", "Captures live weather and saves a dated report"),
      ("Single file", "Assignment1_Weather_Data.py"), ("Needs", "Windows · Chrome · Internet access"),
      ("Folder", f"{P3S}/Assignment-1-PyAutoGUI_Weather_Data")]),
    (f"{P3}/PyAutoGUI Automation/Assignment-2-PyAutoGUI_Bot_Stock_Price/Apple Stock Price Bot.pdf", P3,
     "Apple Stock Price Bot", "Google Finance to a formatted Excel report",
     [("Track", "PyAutoGUI - desktop automation"), ("What it does", "Captures the AAPL quote and builds a dated workbook"),
      ("Single file", "daily_report_bot.py"), ("Needs", "Windows · Chrome · Microsoft Excel"),
      ("Folder", f"{P3S}/Assignment-2-PyAutoGUI_Bot_Stock_Price")]),
    (f"{P3}/Playwright Automation/Playwright Automation.pdf", P3, "Playwright Automation",
     "Browser RPA - driving the page, not the screen",
     [("Track", "Playwright - browser automation"), ("Contents", "Two fundamentals scripts and two complete projects"),
      ("Level", "Intermediate"), ("Needs", "Python 3.10+ · Playwright · Chromium"), ("Folder", P3P)]),
    (f"{P3}/Playwright Automation/Playwright Assignment/WhatsApp Automation Bot.pdf", P3,
     "WhatsApp Automation Bot", "Consent-based messaging, monitored and reported",
     [("Track", "Playwright - browser automation"), ("What it does", "Messages, watches for replies, reports the outcome"),
      ("Single file", "Playwright-WhatsApp-Automation-Bot.py"), ("Needs", "Microsoft Edge · a WhatsApp account · openpyxl"),
      ("Folder", f"{P3P}/Playwright Assignment")]),
    (f"{P3}/Playwright Automation/Playwright Automation Project/SauceDemo Product Automation.pdf", P3,
     "SauceDemo Product Automation", "Sign in, extract every product, report it",
     [("Track", "Playwright - browser automation"), ("What it does", "Extracts products, screenshots them, writes Excel"),
      ("Single file", "Playwright_Web_Automation.py"), ("Needs", "Playwright + Chromium · openpyxl"),
      ("Folder", f"{P3P}/Playwright Automation Project")]),
    (f"{P4}/FirstAPI/FastAPI Calculator API.pdf", P4, "FastAPI Calculator API",
     "Build, validate, and test a real JSON API in Python",
     [("Document", "A practical build guide with the complete source"), ("Level", "Beginner to Intermediate"),
      ("Tools", "Python 3.9+ · FastAPI · Pydantic · Uvicorn"), ("Source file", "calculator.py"),
      ("Phase", "Phase-004 - Interfaces and APIs"), ("Folder", f"{P4}/FirstAPI")]),
    (f"{P4}/FirstAPI/FastAPI App Assignments/GenAI_Architect_Basic_FastAPI_App_Assignment.pdf", P4,
     "Basic FastAPI App", "Project brief and build specification",
     [("Goal", "Build a very basic web API using FastAPI"), ("Difficulty", "Beginner"), ("Tools", "Python · FastAPI · Uvicorn"),
      ("Single file", "main.py"), ("Phase", "Phase-004 - Interfaces and APIs"), ("Folder", "…/FirstAPI/FastAPI App Assignments")]),
    (f"{P4}/Streamlit/Introduction to Streamlit.pdf", P4, "Streamlit", "From Python Script to Interactive MVP",
     [("Document", "A practical, step-by-step beginner's guide"), ("Level", "Beginner - no web development experience required"),
      ("Tools", "Python 3 · Streamlit · Windows Command Prompt"), ("Phase", "Phase-004 - Interfaces and APIs"),
      ("You will build", "A working Calculator MVP that runs in the browser"), ("Folder", f"{P4}/Streamlit")]),
    (f"{P4}/Streamlit/Streamlit Assignment Details/GenAI_Architect_Streamlit_Grade_App_Assignment.pdf", P4,
     "Student Grade App", "Project brief and build specification",
     [("Goal", "Turn a mark into a letter grade in the browser"), ("Difficulty", "Beginner to Medium"), ("Tools", "Python · Streamlit"),
      ("Single file", "grade_app.py"), ("Phase", "Phase-004 - Interfaces and APIs"), ("Folder", "…/Streamlit/Streamlit Assignment Details")]),
]

INSERT_COVERS = [
    ("Phase-005-LLM-Foundations-and-Practical-Tools/LLM-Foundations-and-Practical-Tools-Part-1.pdf",
     "Phase-005-LLM-Foundations-and-Practical-Tools", "LLM Foundations and Practical Tools — Part 1",
     "Foundations and the Closed Path",
     [("Document", "Part 1 of 3 — Foundations and the Closed Path"), ("Pages", "Original pages 1–14 of 37"),
      ("In this part", "01 · LLM and Its Types"), ("", "02 · Open-Source LLM vs Cloud LLM"), ("", "03 · Closed-Source LLM")],
     "PART 1 OF 3  ·  COVER"),
    ("Transformer-Explorer-Guide/Transformer-Explorer-Guide-Part-1.pdf", "Transformer-Explorer-Guide",
     "Transformer Explorer — Part 1", "Start Here and Lessons 01–11",
     [("Document", "Part 1 of 2 — Start Here and Lessons 01–11"), ("Pages", "Original pages 1–13 of 24"),
      ("In this part", "Your first five minutes"), ("", "Lessons 01–07 · Transformer basics, embeddings, position"),
      ("", "Lessons 08–11 · Self-attention, Q/K/V, multi-head, masking")],
     "PART 1 OF 2  ·  COVER"),
]


def main():
    for rel, folder, title, subtitle, facts in COVERS:
        src = REPO / rel
        doc = fitz.open(src)
        n = doc.page_count
        cover = _cover_pdf(folder, title, subtitle, facts, f"PAGE 1 / {n}")
        doc.delete_page(0)
        doc.insert_pdf(cover, start_at=0)
        _save(doc, src)
        print(f"cover      {n:2d}p  {rel}")
    for rel, folder, title, subtitle, facts, label in INSERT_COVERS:
        src = REPO / rel
        doc = fitz.open(src)
        cover = _cover_pdf(folder, title, subtitle, facts, label)
        if "brand-cover" in (doc.metadata.get("keywords") or ""):
            doc.delete_page(0)                  # refresh the cover inserted on an earlier run
            doc.insert_pdf(cover, start_at=0)
            _save(doc, src)
            print(f"cover      (refreshed)  {rel}")
            continue
        doc.insert_pdf(cover, start_at=0)
        m = doc.metadata
        m["keywords"] = (m.get("keywords") or "") + ", brand-cover"
        doc.set_metadata(m)
        n = doc.page_count
        _save(doc, src)
        print(f"cover +1   {n:2d}p  {rel}")
    # covers of split parts 2..K (first page is already a brand cover)
    from rebrand_existing import SPLITS
    for job in SPLITS:
        k_total = len(job["parts"])
        orig_total = job["parts"][-1]["pages"][1]
        for k, part in enumerate(job["parts"], start=1):
            if k == 1:
                continue
            rel = f"{Path(job['src']).parent.as_posix()}/{job['base']}-Part-{k}.pdf"
            src = REPO / rel
            a, b = part["pages"]
            facts = [("Document", f"Part {k} of {k_total} — {part['name']}"),
                     ("Pages", f"Original pages {a}–{b} of {orig_total}")]
            facts += [("In this part", t) if j == 0 else ("", t) for j, t in enumerate(part["topics"])]
            cover = _cover_pdf(job["folder"], f"{job['short']} — Part {k}", part["name"], facts,
                               f"PART {k} OF {k_total}  ·  COVER")
            doc = fitz.open(src)
            doc.delete_page(0)
            doc.insert_pdf(cover, start_at=0)
            _save(doc, src)
            print(f"cover      (part)  {rel}")


if __name__ == "__main__":
    main()
