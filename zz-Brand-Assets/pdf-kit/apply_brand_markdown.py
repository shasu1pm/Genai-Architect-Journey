"""Idempotent brand pass for Genai-Architect-Journey (Markdown + notebooks).

Run:  python zz-Brand-Assets/pdf-kit/apply_brand_markdown.py .   (from the repository root)
Re-running makes no further changes (marker-guarded).
"""
import json, os, re, sys, uuid

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from social import markdown_row  # noqa: E402
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
ASSETS = "zz-Brand-Assets"
SKIP_DIRS = {".git", "venv", ".venv", "__pycache__", "node_modules", "explainers"}
SKIP_FILES = {"My-GitHub-Branding-Instruction.md"}
# Private branding instructions (every edition, e.g. "Master-My-GitHub-Branding-Instruction[18-11-26].md")
# are never branded or rewritten by this tool.
PROTECTED = re.compile(r"^(master-)?my-github-branding-instruction.*\.md$", re.IGNORECASE)
BRAND = "Shasu Vathanan - GEN AI - Product Manager"
changed = []


def rel_prefix(path: Path) -> str:
    depth = len(path.parent.relative_to(ROOT).parts)
    return "../" * depth


def walk(ext):
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for f in fns:
            if f.endswith(ext) and f not in SKIP_FILES and not PROTECTED.match(f):
                yield Path(dp) / f


def read(p):
    raw = p.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    return raw.replace("\r\n", "\n"), nl


def write(p, text, nl):
    if PROTECTED.match(p.name):          # second safeguard: refuse to write a protected instruction file
        raise RuntimeError(f"Refusing to modify protected instruction file: {p.name}")
    p.write_bytes(text.replace("\n", nl).encode("utf-8"))
    changed.append(str(p.relative_to(ROOT)))


# ---------------------------------------------------------------- Markdown
def md_header(R, root=False):
    if root:
        return f"""<!-- brand:header:start -->
<p align="center">
  <img src="{R}{ASSETS}/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="84">
  &nbsp;&nbsp;
  <img src="{R}{ASSETS}/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="76">
</p>
<p align="center">
  <img src="{R}{ASSETS}/SHASUVATHANAN-NAME.png" alt="SHASU VATHANAN" width="420">
  <br><br>
  <img src="{R}{ASSETS}/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="{BRAND}" width="460">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm/Genai-Architect-Journey">GitHub</a>
</p>
<!-- brand:header:end -->

"""
    return f"""<!-- brand:header:start -->
<p align="center">
  <img src="{R}{ASSETS}/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="{R}{ASSETS}/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="{BRAND}" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

"""


def md_footer(R, root=False):
    back = (f'<a href="{ASSETS}/">Brand assets</a>' if root
            else f'<a href="{R}README.md">Back to the journey index</a>')
    return f"""
<!-- brand:footer:start -->
{markdown_row(R)}
<p align="center">
  <img src="{R}{ASSETS}/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>{BRAND}</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; {back}</sub>
</p>
<!-- brand:footer:end -->
"""


for p in walk(".md"):
    text, nl = read(p)
    orig = text
    R = rel_prefix(p)
    root = p.parent == ROOT
    if "<!-- brand:header:start -->" not in text:
        text = md_header(R, root) + text
    if "<!-- brand:footer:start -->" not in text:
        text = text.rstrip("\n") + "\n" + md_footer(R, root)
    else:   # regenerate the managed footer block so template updates reach every file
        new_footer = md_footer(R, root).strip("\n")
        text = re.sub(r"<!-- brand:footer:start -->.*?<!-- brand:footer:end -->",
                      lambda m: new_footer, text, count=1, flags=re.S)
    if text != orig:
        write(p, text, nl)

# ---------------------------------------------------------------- Notebooks
LABELS = {
    "Phase-002-GenAI-Python-Toolkit": "Phase-002 · GenAI Python Toolkit",
    "Phase-006-LangChain-Ecosystem/Langchain-Components": "Phase-006 · LangChain Ecosystem · LangChain Components",
    "Phase-006-LangChain-Ecosystem/Langchain_Advanced_Model_Integration": "Phase-006 · LangChain Ecosystem · Advanced Model Integration",
    "Phase-007-RAG-Introduction": "Phase-007 · RAG Introduction",
}


def header_src(R, kicker):
    return (f"<!-- brand-header -->\n<div align=\"center\">\n\n"
            f"<img src=\"{R}{ASSETS}/Dragon-Motivation-Logo.png\" alt=\"Dragon Motivation logo\" height=\"64\">\n\n"
            f"**{BRAND}**\n\n"
            "[![Website](https://img.shields.io/badge/Website-SHASUVATHANAN.COM-FF4A62?style=for-the-badge)](https://shasuvathanan.com)\n"
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-shasuvathanan-031273?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shasuvathanan)\n\n"
            "</div>\n\n"
            "$\\textcolor{#FF4A62}{\\rule{26em}{4pt}}$\n\n"
            f"*Gen AI Architect Journey &nbsp;·&nbsp; {kicker}*")


def footer_src(R):
    return ("<!-- brand-footer -->\n$\\textcolor{#FF4A62}{\\rule{20em}{2pt}}$\n\n<div align=\"center\">\n\n"
            f"<img src=\"{R}{ASSETS}/NeGot-My-AI-Avatar.png\" alt=\"NeGot - my AI avatar\" height=\"56\">\n\n"
            "**Created and Maintained by**\n\n"
            f"### {BRAND}\n\n"
            "[SHASUVATHANAN.COM](https://shasuvathanan.com) &nbsp;&#8226;&nbsp; [LinkedIn](https://www.linkedin.com/in/shasuvathanan)\n\n"
            + markdown_row(R) + "\n\n"
            "</div>")


SOCIAL_ANCHOR = '[SHASUVATHANAN.COM](https://shasuvathanan.com) &nbsp;&#8226;&nbsp; [LinkedIn](https://www.linkedin.com/in/shasuvathanan)\n'


def add_social_to_footer_cell(text, R):
    """Insert the social row into an existing notebook footer cell (text-level, keeps layout)."""
    if "brand:social:start" in text:
        # remove the previously generated row so the current one (from social.py) is re-inserted
        text = re.sub(r'    "\\n",\n    "<!-- brand:social:start -->\\n",\n.*?    "<!-- brand:social:end -->\\n",\n',
                      "", text, count=1, flags=re.S)
    anchor_json = "    " + json.dumps(SOCIAL_ANCHOR, ensure_ascii=False) + ",\n"
    if text.count(anchor_json) != 1:
        return text
    lines = ["\n"] + [l + "\n" for l in markdown_row(R).split("\n")]
    block = "".join("    " + json.dumps(l, ensure_ascii=False) + ",\n" for l in lines)
    return text.replace(anchor_json, anchor_json + block)


def cell_text(src, with_id):
    lines = src.split("\n")
    cell = {"cell_type": "markdown"}
    if with_id:
        cell["id"] = uuid.uuid4().hex[:8]
    cell["metadata"] = {}
    cell["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    dumped = json.dumps(cell, indent=1, ensure_ascii=False)
    return "\n".join("  " + l for l in dumped.split("\n"))


TQDM_PATH = re.compile(r"c:\\\\Users\\\\THIRU", re.I)

nbs = sorted(walk(".ipynb"))
for p in nbs:
    text, nl = read(p)
    orig = text
    R = rel_prefix(p)
    relp = p.relative_to(ROOT).as_posix()

    # --- Phase-004 Streamlit notebooks: repair existing brand cells
    if "Streamlit Resources" in relp:
        text = text.replace("../../../1-Dragon-Motivation-Logo.png",
                            f"{R}{ASSETS}/Dragon-Motivation-Logo.png")
        if "NeGot-My-AI-Avatar" not in text:
            old = '    "**Created and Maintained by**\\n",\n'
            assert text.count(old) == 1, relp
            neg = (f'    "<img src=\\"{R}{ASSETS}/NeGot-My-AI-Avatar.png\\" alt=\\"NeGot - my AI avatar\\" height=\\"56\\">\\n",\n'
                   '    "\\n",\n')
            text = text.replace(old, neg + old)
    else:
        # --- content fixes (new phases only)
        if relp.endswith("Phase-007-RAG-Introduction/06_BM25_Rerank.ipynb"):
            text = text.replace('"# 7. BM25 & Rerank\\n"', '"# 6. BM25 & Rerank\\n"')
        if relp.endswith("01_Model_Integration.ipynb"):
            text = text.replace("The main model in this course is", "The main model in this phase is")
        # --- drop stderr warnings that expose another machine's local path
        if relp.startswith("Phase-006") and TQDM_PATH.search(text):
            nb = json.loads(text)
            for c in nb["cells"]:
                if c.get("outputs"):
                    c["outputs"] = [o for o in c["outputs"]
                                    if not (o.get("output_type") == "stream" and o.get("name") == "stderr"
                                            and "Users\\THIRU" in "".join(o.get("text", [])))]
            text = json.dumps(nb, indent=1, ensure_ascii=False) + "\n"
        # --- brand header/footer cells
        if "<!-- brand-header -->" not in text:
            folder = p.parent.relative_to(ROOT).as_posix()
            label = LABELS.get(folder) or " · ".join(
                part.replace("-", " ", 0) for part in folder.split("/"))
            siblings = sorted(x for x in nbs if x.parent == p.parent)
            kicker = f"{label} &nbsp;·&nbsp; Notebook {siblings.index(p) + 1} of {len(siblings)}"
            with_id = '"id":' in text
            text = re.sub(r'^\{\n "cells": \[\n',
                          lambda m: m.group(0) + cell_text(header_src(R, kicker), with_id) + ",\n", text, count=1)
            text = re.sub(r'\n \],\n "metadata"',
                          lambda m: ",\n" + cell_text(footer_src(R), with_id) + m.group(0), text, count=1)
    # --- social links row in the footer cell (all notebooks)
    text = add_social_to_footer_cell(text, R)
    if text != orig:
        json.loads(text)  # must stay valid JSON
        write(p, text, nl)

print(len(changed), "files changed")
for c in changed:
    print("  ", c)
