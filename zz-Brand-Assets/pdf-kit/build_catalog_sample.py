"""Rebuild Phase-008's RAG knowledge source, `products_catalog.pdf`, with the brand.

`rag.py` reads this PDF with pypdf, splits the text on "Product Name:" (one chunk per
product, plus one intro chunk) and stores the chunks in ChromaDB. The original text is kept
verbatim in `sources/products_catalog.txt`; this script re-typesets it with the brand cover,
header and footer. Two checks run after the build:

1. word survival — every word of the source appears in the rebuilt PDF;
2. chunking     — the exact splitting logic of `rag.py` still yields one chunk per product,
                  and each chunk carries that product's own ID, category, price and details.

ShopEasy is a hypothetical store; the catalogue is sample data for the demo.

Run:  python zz-Brand-Assets/pdf-kit/build_catalog_sample.py
Delete `Phase-008-RAG-Agent-Explained/chroma_db/` afterwards so the index is rebuilt.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand_pdf import (BLUE, CORAL, INK, TINT, W, LM, RM, Paragraph, ParagraphStyle,  # noqa: E402
                       Spacer, _md, build, callout, h1, lead)
from reportlab.platypus import KeepTogether, Table, TableStyle  # noqa: E402

KIT = Path(__file__).resolve().parent
REPO = KIT.parents[1]
FOLDER = "Phase-008-RAG-Agent-Explained"
SRC = KIT / "sources" / "products_catalog.txt"
OUT = REPO / FOLDER / "products_catalog.pdf"

NAME = ParagraphStyle("pn", fontName="Calibri-Bold", fontSize=11.4, leading=14.5, textColor=BLUE, spaceAfter=2)
LINE = ParagraphStyle("pl", fontName="Calibri", fontSize=9.6, leading=12.8, textColor=INK, spaceAfter=0)


def parse(text: str):
    """Return (title, intro lines, products) where each product is a list of 'Label: value' lines."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    title, intro, products = lines[0], [], []
    for line in lines[1:]:
        if line.startswith("Product Name:"):
            products.append([line])
        elif products:
            products[-1].append(line)
        else:
            intro.append(line)
    return title, intro, products


def card(fields):
    """One product as a tinted card. Lines stay in source order so text extraction is unchanged."""
    label, _, value = fields[0].partition(":")
    rows = [Paragraph(f"{label}: <font color='#FF4A62'>{_md(value.strip())}</font>", NAME)]
    for f in fields[1:]:
        k, _, v = f.partition(":")
        rows.append(Paragraph(f"<b>{_md(k)}:</b> {_md(v.strip())}", LINE))
    t = Table([[rows]], colWidths=[W - LM - RM])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TINT),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.6, CORAL),
                           ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    return KeepTogether([t, Spacer(1, 7)])


def rag_chunks(full_text: str):
    """The splitting logic of Phase-008 rag.py, reproduced for the check."""
    parts = full_text.split("Product Name:")
    intro = parts[0].strip()
    chunks = [intro] if intro else []
    for part in parts[1:]:
        if part.strip() != "":
            chunks.append("Product Name:" + part.strip())
    return chunks


def words(t):
    return re.findall(r"[A-Za-z0-9]+", t)


def main():
    import fitz
    from collections import Counter
    from pypdf import PdfReader

    src_text = SRC.read_text(encoding="utf-8")
    title, intro, products = parse(src_text)
    story = []
    story.extend(h1(title))
    story.extend(lead(l) for l in intro)
    story.extend(callout("Sample data — hypothetical store",
                         "ShopEasy is a made-up online store. This catalogue is the knowledge source of the "
                         "Phase-008 RAG agent: `rag.py` reads it, keeps one chunk per product and stores the "
                         "chunks in ChromaDB, and the `search_products` tool answers from them."))
    story.extend(card(p) for p in products)
    build(OUT, folder=FOLDER, title="ShopEasy Product Catalogue", short="ShopEasy Product Catalogue",
          subtitle="Twelve sample products with ID, category, price and details — the knowledge source of the RAG agent",
          facts=[("Document", "Sample product catalogue (hypothetical store)"),
                 ("Used by", "rag.py — read with pypdf, one chunk per product, stored in ChromaDB"),
                 ("Contents", f"{len(products)} products · Electronics, Accessories, Wearables, Fitness, Kitchen"),
                 ("Answered through", "search_products — an MCP tool used by the CrewAI shopping agent"),
                 ("Folder", FOLDER)],
          story=story, keywords="RAG sample, product catalogue, ChromaDB, MCP, CrewAI")

    # check 1: every source word survives (order-insensitive multiset check)
    src = Counter(words(src_text))
    out = Counter(words("".join(pg.get_text() for pg in fitz.open(OUT))))
    missing = {w: n - out[w] for w, n in src.items() if out[w] < n}

    # check 2: rag.py chunking on the rebuilt PDF (pypdf, exactly as rag.py reads it)
    full = "".join(pg.extract_text() + "\n" for pg in PdfReader(str(OUT)).pages)
    chunks = rag_chunks(full)
    problems = []
    if len(chunks) != len(products) + 1:
        problems.append(f"expected {len(products) + 1} chunks, got {len(chunks)}")
    for prod, chunk in zip(products, chunks[1:]):
        for line in prod:
            if "".join(line.split()) not in "".join(chunk.split()):   # rag.py drops the space after "Name:"
                problems.append(f"{prod[0]!r}: missing {line!r}")
    n = fitz.open(OUT).page_count
    print(f"{n}p  {OUT.relative_to(REPO)}  missing words: {missing or 'none'}  "
          f"chunks: {len(chunks)}  chunk problems: {problems or 'none'}")


if __name__ == "__main__":
    main()
