"""Re-brand existing PDFs without touching their learning content.

For every page: the old header band and old footer band are redacted (removed, filled
white) and the current brand header/footer from `brand_pdf.py` is stamped in their place.
Body pages are otherwise untouched. PDFs over 15 pages are split into parts at topic
boundaries; each extra part gets a branded cover. Metadata is set to the brand.

A safety check runs first: if any body element crosses a band edge the PDF is skipped
and reported, so learning content can never be clipped.

Run:  python rebrand_existing.py            (from anywhere; paths are repo-relative)
"""
from __future__ import annotations

import io
import shutil
import sys
from pathlib import Path

import fitz  # PyMuPDF
from reportlab.pdfgen import canvas

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brand_pdf as B  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
W, H = B.W, B.H

# Band profiles: (header_cut, footer_cut) in top-down points.
PROFILES = {
    "A": (80, 788),   # Phase-001 .. Phase-004 generator (body 92 .. 781)
    "B": (84, 775),   # Phase-005 generator (body 91 .. 771)
    "T": (80, 795),   # Transformer guide, Chromium-rendered (body 88 .. ~790)
}

P3 = "Phase-003-Robotic-Process-Automation-(RPA)"
P4 = "Phase-004-FastAPI-And-Streamlit"
JOBS = [
    # (relative path, exact folder name for the header, short title, profile, cover_has_header)
    ("Phase-001-Programming-Foundations/Student Grade System.pdf",
     "Phase-001-Programming-Foundations", "Student Grade System", "A", False),
    ("Phase-002-GenAI-Python-Toolkit/Mandatory Python Concepts for Generative AI.pdf",
     "Phase-002-GenAI-Python-Toolkit", "Mandatory Python Concepts for Generative AI", "A", False),
    (f"{P3}/RPA - Robotic Process Automation.pdf", P3, "RPA - Robotic Process Automation", "A", False),
    (f"{P3}/PyAutoGUI Automation/PyAutoGUI Automation.pdf", P3, "PyAutoGUI Automation", "A", False),
    (f"{P3}/PyAutoGUI Automation/Assignment-1-PyAutoGUI_Weather_Data/Bengaluru Weather Bot.pdf",
     P3, "Bengaluru Weather Bot", "A", False),
    (f"{P3}/PyAutoGUI Automation/Assignment-2-PyAutoGUI_Bot_Stock_Price/Apple Stock Price Bot.pdf",
     P3, "Apple Stock Price Bot", "A", False),
    (f"{P3}/Playwright Automation/Playwright Automation.pdf", P3, "Playwright Automation", "A", False),
    (f"{P3}/Playwright Automation/Playwright Assignment/WhatsApp Automation Bot.pdf",
     P3, "WhatsApp Automation Bot", "A", False),
    (f"{P3}/Playwright Automation/Playwright Automation Project/SauceDemo Product Automation.pdf",
     P3, "SauceDemo Product Automation", "A", False),
    (f"{P4}/FirstAPI/FastAPI Calculator API.pdf", P4, "FastAPI Calculator API", "A", False),
    (f"{P4}/FirstAPI/FastAPI App Assignments/GenAI_Architect_Basic_FastAPI_App_Assignment.pdf",
     P4, "Basic FastAPI App", "A", False),
    (f"{P4}/Streamlit/Introduction to Streamlit.pdf", P4, "Introduction to Streamlit", "A", False),
    (f"{P4}/Streamlit/Streamlit Assignment Details/GenAI_Architect_Streamlit_Grade_App_Assignment.pdf",
     P4, "Student Grade App", "A", False),
]

# Over-length PDFs: split into parts at topic boundaries (1-based inclusive page ranges).
SPLITS = [
    dict(src="Phase-005-LLM-Foundations-and-Practical-Tools/LLM-Foundations-and-Practical-Tools.pdf",
         folder="Phase-005-LLM-Foundations-and-Practical-Tools",
         short="LLM Foundations and Practical Tools", profile="B", cover_has_header=False,
         base="LLM-Foundations-and-Practical-Tools",
         parts=[
             dict(pages=(1, 14), name="Foundations and the Closed Path",
                  topics=["01 · LLM and Its Types", "02 · Open-Source LLM vs Cloud LLM",
                          "03 · Closed-Source LLM"]),
             dict(pages=(15, 26), name="Access, Benchmarks and the Toolkit",
                  topics=["04 · How to Purchase API Keys for Closed LLMs", "05 · LLM Benchmarks",
                          "06 · Essential AI Tools", "07 · Hugging Face Spaces"]),
             dict(pages=(27, 37), name="The Open Path — Running Models Locally",
                  topics=["08 · Pulling an Open-Source Model from Hugging Face",
                          "09 · Running an Open-Source Model Using Ollama",
                          "10 · Open-Source Model with Ollama — Hands-On Practice"]),
         ]),
    dict(src="Transformer-Explorer-Guide/Transformer-Explorer-Guide.pdf",
         folder="Transformer-Explorer-Guide", short="Transformer Explorer", profile="T",
         cover_has_header=True, base="Transformer-Explorer-Guide",
         parts=[
             dict(pages=(1, 13), name="Start Here and Lessons 01–11",
                  topics=["Your first five minutes", "Lessons 01–03 · What a Transformer is and how it works",
                          "Lessons 04–07 · Embedding, position and repeated blocks",
                          "Lessons 08–11 · Self-attention, Q/K/V, multi-head, masking"]),
             dict(pages=(14, 24), name="Lessons 12–20, Experiments and Reference",
                  topics=["Lessons 12–14 · Attention output, MLP and output logits",
                          "Lessons 15–17 · Probabilities, temperature and sampling",
                          "Lessons 18–20 · Residual connections, layer norm and dropout",
                          "Four experiments · Reference and educational source"]),
         ]),
]


# --------------------------------------------------------------------------- helpers
def _overlay_page(folder, short, label, with_header):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    if with_header:
        B.draw_header(c, folder, short)
    B.draw_footer(c, label)
    c.showPage()
    c.save()
    return fitz.open("pdf", buf.getvalue())


def _cover_pdf(folder, title, subtitle, facts, label):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    B.draw_cover(c, folder, title, subtitle, facts)
    B.draw_footer(c, label)
    c.showPage()
    c.save()
    return fitz.open("pdf", buf.getvalue())


def _conflicts(page, bands):
    """Elements that cross a band edge (would be clipped). Fully-inside items are old branding."""
    issues = []
    items = [fitz.Rect(b["bbox"]) for b in page.get_text("dict")["blocks"]]
    items += [fitz.Rect(i["bbox"]) for i in page.get_image_info()]
    for d in page.get_drawings():
        if d.get("fill") in ((1.0, 1.0, 1.0),) and d["rect"].width > 500:
            continue  # page/band background
        items.append(fitz.Rect(d["rect"]))
    for r in items:
        r = r & page.rect              # ignore slivers that spill past the page edge
        if r.is_empty:
            continue
        for band in bands:
            inter = r & band
            if not inter.is_empty and inter.height > 0.6 and not band.contains(r):
                issues.append((tuple(round(v) for v in r), tuple(round(v) for v in band)))
    return issues


def _restamp(doc, page_index, folder, short, label, profile, with_header):
    hcut, fcut = PROFILES[profile]
    page = doc[page_index]
    bands = [fitz.Rect(0, fcut, W, H)]
    if with_header:
        bands.append(fitz.Rect(0, 0, W, hcut))
    bad = _conflicts(page, bands)
    if bad:
        raise RuntimeError(f"page {page_index + 1}: body content crosses a band: {bad[:3]}")
    for band in bands:
        page.add_redact_annot(band, fill=(1, 1, 1))
    page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_REMOVE,
                          graphics=fitz.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
                          text=fitz.PDF_REDACT_TEXT_REMOVE)
    ov = _overlay_page(folder, short, label, with_header)
    page.show_pdf_page(page.rect, ov, 0, overlay=True)


def _meta(doc, title, folder, keywords=""):
    doc.set_metadata({
        "title": title, "author": B.BRAND, "subject": folder, "creator": B.BRAND,
        "producer": "Shasu Vathanan brand PDF kit (PyMuPDF + ReportLab)",
        "keywords": ", ".join(x for x in [keywords, "SHASUVATHANAN.COM", "GenAI Architect Journey"] if x),
    })


def _save(doc, dest: Path):
    tmp = dest.with_suffix(".tmp.pdf")
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    shutil.move(tmp, dest)


# --------------------------------------------------------------------------- jobs
def rebrand(rel, folder, short, profile, cover_has_header):
    src = REPO / rel
    doc = fitz.open(src)
    n = doc.page_count
    title = doc.metadata.get("title") or short
    for i in range(n):
        _restamp(doc, i, folder, short, f"PAGE {i + 1} / {n}", profile, with_header=(i > 0 or cover_has_header))
    _meta(doc, title, folder)
    _save(doc, src)
    return n


def split(job):
    src = REPO / job["src"]
    if not src.exists():                     # already split on an earlier run (one-time migration)
        print(f"skip      (already split)  {job['src']}")
        return []
    orig = fitz.open(src)
    total = orig.page_count
    k_total = len(job["parts"])
    outputs = []
    for k, part in enumerate(job["parts"], start=1):
        a, b = part["pages"]
        doc = fitz.open()
        if k > 1:
            facts = [("Document", f"Part {k} of {k_total} — {part['name']}"),
                     ("Pages", f"Original pages {a}–{b} of {total}")]
            facts += [("In this part", t) if j == 0 else ("", t) for j, t in enumerate(part["topics"])]
            cover = _cover_pdf(job["folder"], f"{job['short']} — Part {k}", part["name"], facts,
                               f"PART {k} OF {k_total}  ·  COVER")
            doc.insert_pdf(cover)
        doc.insert_pdf(orig, from_page=a - 1, to_page=b - 1)
        offset = 1 if k > 1 else 0
        for j in range(b - a + 1):
            pno = a + j
            label = f"PART {k} OF {k_total}  ·  PAGE {pno} / {total}"
            with_header = (pno > 1) or job["cover_has_header"]
            _restamp(doc, offset + j, job["folder"], job["short"], label, job["profile"], with_header)
        _meta(doc, f"{job['short']} — Part {k} of {k_total}: {part['name']}", job["folder"])
        dest = src.with_name(f"{job['base']}-Part-{k}.pdf")
        _save(doc, dest)
        outputs.append((dest, b - a + 1 + offset))
    orig.close()
    return outputs


if __name__ == "__main__":
    only = set(sys.argv[1:])
    for job in JOBS:
        if only and not any(o in job[0] for o in only):
            continue
        n = rebrand(*job)
        print(f"rebranded {n:2d}p  {job[0]}")
    for job in SPLITS:
        if only and not any(o in job["src"] for o in only):
            continue
        for dest, n in split(job):
            print(f"split     {n:2d}p  {dest.relative_to(REPO)}")
