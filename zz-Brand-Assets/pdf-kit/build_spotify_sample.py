"""Rebuild Phase-007's RAG sample document with the brand.

`spotify_web_app_architecture.pdf` is the knowledge source that `rag_faiss_app.py` loads.
Its original text is kept verbatim in `sources/spotify_web_app_architecture.txt`; this script
re-typesets that text with the brand cover, header and footer. A check confirms every word
of the source appears in the rebuilt PDF, so RAG answers are unaffected apart from the
brand header/footer lines.

Trademark note: the Spotify logo (sources/spotify-logo.png, cropped from the image the owner
supplied) is shown at the owner's request to identify the app style. It is a registered
trademark of Spotify AB and is always shown with a "not affiliated / not endorsed" notice.

Run:  python zz-Brand-Assets/pdf-kit/build_spotify_sample.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand_pdf import (BLUE, INK, MUTED, S, W, LM, RM, Paragraph, ParagraphStyle, Spacer,  # noqa: E402
                       _md, build, bullets, code, h1, h2, lead, p, small)
from reportlab.lib import colors  # noqa: E402
from reportlab.platypus import Flowable, Table, TableStyle  # noqa: E402

KIT = Path(__file__).resolve().parent
REPO = KIT.parents[1]
SRC = KIT / "sources" / "spotify_web_app_architecture.txt"
OUT = REPO / "Phase-007-RAG-Introduction" / "spotify_web_app_architecture.pdf"
GREEN = colors.HexColor("#1DB954")      # Spotify green, used only for the concept banner accent
LOGO_SPOTIFY = KIT / "sources" / "spotify-logo.png"
GREEN_DARK = colors.HexColor("#14833B")


class LogoImage(Flowable):
    """Draws the supplied third-party logo (kept as its own source file, never in zz-Brand-Assets)."""

    def __init__(self, path, width):
        super().__init__()
        from brand_pdf import _img
        self.ir = _img(path)
        iw, ih = self.ir.getSize()
        self.width, self.height = width, width * ih / iw

    def draw(self):
        self.canv.drawImage(self.ir, 0, 0, width=self.width, height=self.height, mask="auto")


class MusicMark(Flowable):
    """A generic music-app mark: green rounded tile with two beamed notes and sound waves."""

    def __init__(self, size=58):
        super().__init__()
        self.width = self.height = size

    def draw(self):
        c, s = self.canv, self.width
        c.setFillColor(GREEN)
        c.roundRect(0, 0, s, s, s * 0.22, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setStrokeColor(colors.white)
        # two note heads
        c.ellipse(s * 0.20, s * 0.20, s * 0.40, s * 0.36, stroke=0, fill=1)
        c.ellipse(s * 0.55, s * 0.28, s * 0.75, s * 0.44, stroke=0, fill=1)
        # stems and beam
        c.setLineWidth(s * 0.055)
        c.line(s * 0.385, s * 0.29, s * 0.385, s * 0.74)
        c.line(s * 0.735, s * 0.37, s * 0.735, s * 0.82)
        c.setLineWidth(s * 0.11)
        c.line(s * 0.385, s * 0.70, s * 0.735, s * 0.78)


def concept_banner():
    sty = ParagraphStyle("cb", parent=S["p"], fontSize=9.4, leading=12.6, textColor=INK, spaceAfter=0)
    tsty = ParagraphStyle("cbt", parent=S["callt"], textColor=GREEN_DARK)
    text = [Paragraph("Concept document — a hypothetical Spotify-like music streaming web app", tsty),
            Paragraph("Sample architecture used as the knowledge source for the Phase-007 RAG demo "
                      "(<font name='Consolas'>rag_faiss_app.py</font>). The Spotify logo identifies the app style "
                      "this concept is modelled on. Spotify and the Spotify logo are registered trademarks of "
                      "Spotify AB; this document is not affiliated with, endorsed by or produced by Spotify.", sty)]
    t = Table([[LogoImage(LOGO_SPOTIFY, 128), text]], colWidths=[148, W - LM - RM - 148])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EEFAF2")),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.6, GREEN),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    return [t, Spacer(1, 10)]


def parse(lines):
    story, items, para, pre = [], [], [], []
    title = None

    def flush():
        nonlocal items, para, pre
        if items:
            story.extend(bullets(items)); items = []
        if para:
            story.append(p(" ".join(para))); para = []
        if pre:
            story.extend(code("\n".join(pre))); pre = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        s = line.strip()
        if not s:
            flush(); i += 1; continue
        if re.fullmatch(r"=+", nxt):
            flush(); title = s; i += 2; continue
        if re.fullmatch(r"-{3,}", nxt):
            flush(); story.extend(h1(s)); i += 2; continue
        if re.match(r"^\d+\) ", s) or re.match(r"^[A-M]\. ", s):
            flush(); story.extend(h2(s)); i += 1; continue
        if line.startswith("  ") and s.startswith("- "):          # indented route lists keep alignment
            if items or para:
                flush()
            pre.append(line.strip()[2:]); i += 1; continue
        if pre:
            flush()
        if s.startswith("- "):
            if para:
                flush()
            items.append(s[2:]); i += 1; continue
        if s.endswith(":") and len(s) < 70 and s[0].isupper():   # sub-label such as "Backend:"
            flush(); story.append(Paragraph(f"<b>{_md(s)}</b>", S["p"])); i += 1; continue
        if items:                                               # wrapped continuation of a bullet
            items[-1] += " " + s; i += 1; continue
        para.append(s); i += 1
    flush()
    return title, story


def cover_logo(c):
    """Spotify logo centred below the facts table, with its trademark line."""
    from brand_pdf import H, _img
    ir = _img(LOGO_SPOTIFY)
    iw, ih = ir.getSize()
    w = 150
    h = w * ih / iw
    x, y = (W - w) / 2, 200
    c.drawImage(ir, x, y, width=w, height=h, mask="auto")
    c.setFont("Calibri", 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y - 12, "Spotify and the Spotify logo are registered trademarks of Spotify AB. "
                        "Not affiliated with or endorsed by Spotify.")


def words(t):
    return re.findall(r"[A-Za-z0-9]+", t)


def main():
    import fitz
    lines = SRC.read_text(encoding="utf-8").splitlines()
    title, body = parse(lines)
    story = []
    story.extend(h1(title))
    story.extend(concept_banner())
    story.extend(body)
    build(OUT, folder="Phase-007-RAG-Introduction", title="Spotify-like Web App",
          short="Spotify-like Web App — Sample Architecture",
          subtitle="Full architecture and feature list for a hypothetical music streaming web app — the RAG demo knowledge source",
          facts=[("Document", "Sample architecture document (concept, not a real product)"),
                 ("Used by", "rag_faiss_app.py — loaded with PyPDFLoader and indexed in FAISS"),
                 ("Scale target", "100,000+ daily users"),
                 ("Affiliation", "Not affiliated with or endorsed by Spotify"),
                 ("Folder", "Phase-007-RAG-Introduction")],
          story=story, keywords="RAG sample, architecture, music streaming, microservices",
          cover_extra=cover_logo)
    # verify: every source word survives (order-insensitive multiset check)
    from collections import Counter
    src = Counter(words(SRC.read_text(encoding="utf-8")))
    out = Counter(words("".join(pg.get_text() for pg in fitz.open(OUT))))
    missing = {w: n - out[w] for w, n in src.items() if out[w] < n}
    n = fitz.open(OUT).page_count
    print(f"{n}p  {OUT.relative_to(REPO)}  missing words: {missing or 'none'}")


if __name__ == "__main__":
    main()
