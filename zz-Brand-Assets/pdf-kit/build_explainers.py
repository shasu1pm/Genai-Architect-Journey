"""Build one branded explainer PDF per folder from a small Markdown source.

Sources live in `pdf-kit/explainers/*.md`. Each file starts with a front-matter block:

    ---
    out: Phase-001-Programming-Foundations/Programming-Foundations-Explainer.pdf
    folder: Phase-001-Programming-Foundations
    title: Programming Foundations
    subtitle: One-line purpose shown on the cover
    fact: Document | Phase explainer
    fact: Level | Beginner
    ---

Body syntax (deliberately small):
    # Heading 1            ## Heading 2
    lead: one coloured lead sentence
    flow: Step A > Step B > Step C
    - bullet
    | table | header |  (GitHub table; the separator row is skipped)
    ```lang Title        (fenced code; optional title after the language)
    > [!NOTE] Title  /  > [!TIP] Title   then `> text` lines   (callout)
    _note: small italic note
    anything else = paragraph (consecutive lines are joined)

Run:  python zz-Brand-Assets/pdf-kit/build_explainers.py [name-filter ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand_pdf import build, bullets, callout, code, flow, h1, h2, lead, p, small, table  # noqa: E402

KIT = Path(__file__).resolve().parent
REPO = KIT.parents[1]
SRC = KIT / "explainers"


def parse(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta, facts = {}, []
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if k == "fact":
            a, _, b = v.partition("|")
            facts.append((a.strip(), b.strip()))
        elif k:
            meta[k] = v
    meta["facts"] = facts
    body = text[m.end():].splitlines()

    story, i, para = [], 0, []

    def flush():
        if para:
            story.append(p(" ".join(para)))
            para.clear()

    while i < len(body):
        line = body[i]
        s = line.strip()
        if not s:
            flush(); i += 1; continue
        if s.startswith("```"):
            flush()
            head = s[3:].strip().split(" ", 1)
            title = head[1] if len(head) > 1 else None
            buf = []
            i += 1
            while not body[i].strip().startswith("```"):
                buf.append(body[i]); i += 1
            story += code("\n".join(buf), title)
            i += 1; continue
        if s.startswith("## "):
            flush(); story += h2(s[3:]); i += 1; continue
        if s.startswith("# "):
            flush(); story += h1(s[2:]); i += 1; continue
        if s.startswith("lead:"):
            flush(); story.append(lead(s[5:].strip())); i += 1; continue
        if s.startswith("flow:"):
            flush(); story += flow([x.strip() for x in s[5:].split(">")]); i += 1; continue
        if s.startswith("_note:"):
            flush(); story.append(small(s[6:].strip())); i += 1; continue
        if s.startswith("> [!"):
            flush()
            kind = "tip" if "[!TIP]" in s else "note"
            title = s.split("]", 1)[1].strip()
            buf = []
            i += 1
            while i < len(body) and body[i].strip().startswith(">"):
                buf.append(body[i].strip()[1:].strip()); i += 1
            story += callout(title, [" ".join(buf)], kind)
            continue
        if s.startswith("- "):
            flush()
            items = []
            while i < len(body) and body[i].strip().startswith("- "):
                items.append(body[i].strip()[2:]); i += 1
            story += bullets(items)
            continue
        if s.startswith("|"):
            flush()
            rows = []
            while i < len(body) and body[i].strip().startswith("|"):
                cells = [c.strip() for c in body[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            header, data = rows[0], rows[1:]
            widths = None
            if "widths" in meta and len(header) == 2:
                widths = [float(x) for x in meta["widths"].split(",")]
            story += table(header, data, widths)
            continue
        para.append(s)
        i += 1
    flush()
    return meta, story


def main(filters):
    import fitz
    for src in sorted(SRC.glob("*.md")):
        if filters and not any(f in src.name for f in filters):
            continue
        meta, story = parse(src)
        out = REPO / meta["out"]
        build(out, folder=meta["folder"], title=meta["title"], subtitle=meta["subtitle"],
              facts=meta["facts"], story=story, short=meta.get("short", meta["title"]),
              kicker=meta.get("kicker"), keywords=meta.get("keywords", ""))
        n = fitz.open(out).page_count
        flag = "" if n <= 10 else ("  (over target 10)" if n <= 15 else "  ** OVER 15 **")
        print(f"{n:3d}p  {meta['out']}{flag}")


if __name__ == "__main__":
    main(sys.argv[1:])
