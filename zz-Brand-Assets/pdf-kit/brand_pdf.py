"""Brand PDF engine — Shasu Vathanan - GEN AI - Product Manager.

One place that defines how every PDF in the Genai-Architect-Journey repository looks:
cover, page header, page footer, colours, fonts and content blocks. Used by
`build_docs.py` (new explainer PDFs) and `rebrand_existing.py` (re-branding
existing PDFs without touching their body pages).

All artwork comes from `zz-Brand-Assets/` (this file's grandparent folder).
"""
from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Preformatted, Spacer, Table, TableStyle)

# --------------------------------------------------------------------------- identity
BRAND = "Shasu Vathanan - GEN AI - Product Manager"
WEBSITE_TEXT, WEBSITE_URL = "SHASUVATHANAN.COM", "https://shasuvathanan.com"
LINKEDIN_TEXT, LINKEDIN_URL = "linkedin.com/in/shasuvathanan", "https://www.linkedin.com/in/shasuvathanan"
GITHUB_TEXT, GITHUB_URL = "github.com/shasu1pm/Genai-Architect-Journey", "https://github.com/shasu1pm/Genai-Architect-Journey"

ASSETS = Path(__file__).resolve().parents[1]
LOGO = ASSETS / "Dragon-Motivation-Logo.png"                  # 1019 x 1510
NAME = ASSETS / "SHASUVATHANAN-NAME.png"                      # 1863 x 199
STRIP = ASSETS / "ShasuVathanan-GEN AI-Product-Manager.png"   # 2323 x 63
NEGOT = ASSETS / "NeGot-My-AI-Avatar.png"                     # 1254 x 1254

# --------------------------------------------------------------------------- palette (no black)
CORAL = colors.HexColor("#FF4A62")
CORAL2 = colors.HexColor("#FF5A45")
BLUE = colors.HexColor("#031273")
INK = colors.HexColor("#1B2559")
MUTED = colors.HexColor("#5A6391")
HAIR = colors.HexColor("#DDE1F2")
TINT = colors.HexColor("#F2F4FF")
CORAL_TINT = colors.HexColor("#FFF1F3")
WHITE = colors.white

W, H = A4
LM = RM = 46.0

# --------------------------------------------------------------------------- fonts
_FONTS = Path("C:/Windows/Fonts")
for name, file in [("Calibri", "calibri.ttf"), ("Calibri-Bold", "calibrib.ttf"),
                   ("Calibri-Italic", "calibrii.ttf"), ("Calibri-BoldItalic", "calibriz.ttf"),
                   ("Consolas", "consola.ttf"), ("Consolas-Bold", "consolab.ttf")]:
    if name not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont(name, str(_FONTS / file)))
pdfmetrics.registerFontFamily("Calibri", normal="Calibri", bold="Calibri-Bold",
                              italic="Calibri-Italic", boldItalic="Calibri-BoldItalic")
pdfmetrics.registerFontFamily("Consolas", normal="Consolas", bold="Consolas-Bold",
                              italic="Consolas", boldItalic="Consolas-Bold")

_img_cache: dict[Path, ImageReader] = {}


def _img(p: Path) -> ImageReader:
    """Load an original brand asset and downscale it IN MEMORY (max 480 px on the long side)
    so PDFs stay light. The files in zz-Brand-Assets/ are never modified or copied."""
    if p not in _img_cache:
        from PIL import Image
        from social import open_logo
        im = open_logo(p, 512)
        if "Social-Media-Logos" in str(p):              # small link icons
            im.thumbnail((96, 96), Image.LANCZOS)
        elif max(im.size) > 300 and im.width < 1500:    # logo / NeGot; text lockups stay crisp
            im.thumbnail((300, 300), Image.LANCZOS)
        _img_cache[p] = ImageReader(im)
    return _img_cache[p]


def _draw_img(c, p: Path, x, y_top, w=None, h=None):
    """Draw image with its top-left at (x, y_top) in ReportLab coords; keep aspect."""
    ir = _img(p)
    iw, ih = ir.getSize()
    if w is None:
        w = h * iw / ih
    if h is None:
        h = w * ih / iw
    c.drawImage(ir, x, y_top - h, width=w, height=h, mask="auto")
    return w, h


def gradient_bar(c, x, y, w, h, c1=CORAL, c2=CORAL2, steps=None):
    """Smooth left-to-right coral gradient (#FF4A62 -> #FF5A45) clipped to a rectangle."""
    c.saveState()
    path = c.beginPath()
    path.rect(x, y, w, h)
    c.clipPath(path, stroke=0, fill=0)
    c.linearGradient(x, y, x + w, y, (c1, c2), extend=False)
    c.restoreState()


def _link_text(c, text, x, y, font, size, color, url, align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    tw = pdfmetrics.stringWidth(text, font, size)
    if align == "right":
        x = x - tw
    c.drawString(x, y, text)
    if url:
        c.linkURL(url, (x, y - 1.5, x + tw, y + size), relative=0)
    return tw


# --------------------------------------------------------------------------- header / footer
HEADER_BAND = 80     # points from the top reserved for the header
FOOTER_BAND = 54     # points from the bottom reserved for the footer


def draw_header(c, folder: str, doc_title: str):
    """Logo + name lockup + brand strip on the left; exact folder name, document title and
    website on the right; coral gradient rule underneath."""
    _draw_img(c, LOGO, LM, H - 17, h=42)
    _draw_img(c, NAME, LM + 34, H - 21, w=132)
    _draw_img(c, STRIP, LM + 34, H - 46, w=236)
    right = W - RM
    _link_text(c, folder, right, H - 29, "Calibri-Bold", 7.4, BLUE, None, "right")
    _link_text(c, doc_title.upper(), right, H - 40, "Calibri", 6.8, MUTED, None, "right")
    _link_text(c, WEBSITE_TEXT, right, H - 51, "Calibri-Bold", 6.8, CORAL, WEBSITE_URL, "right")
    gradient_bar(c, LM, H - 68, W - LM - RM, 2.6)


def draw_footer(c, page_label: str):
    """Hairline, NeGot accent, brand line + website/LinkedIn on the left; page label and
    GitHub link on the right."""
    c.setStrokeColor(HAIR)
    c.setLineWidth(0.6)
    c.line(LM, 45, W - RM, 45)
    _draw_img(c, NEGOT, LM, 41, h=29)
    _link_text(c, BRAND, LM + 34, 29, "Calibri-Bold", 7.6, BLUE, None)
    x = LM + 34
    x += _link_text(c, WEBSITE_TEXT, x, 18, "Calibri", 7, MUTED, WEBSITE_URL)
    x += _link_text(c, "   ·   ", x, 18, "Calibri", 7, MUTED, None)
    _link_text(c, LINKEDIN_TEXT, x, 18, "Calibri", 7, MUTED, LINKEDIN_URL)
    right = W - RM
    _link_text(c, page_label, right, 29, "Calibri-Bold", 7.6, CORAL, None, "right")
    _link_text(c, GITHUB_TEXT, right, 18, "Calibri", 6.6, MUTED, GITHUB_URL, "right")


# --------------------------------------------------------------------------- cover
def draw_cover(c, folder: str, title: str, subtitle: str, facts: list[tuple[str, str]],
               kicker: str | None = None):
    """Cover page: centred logo, name lockup and brand strip; coral gradient hero with the
    exact folder name, title and purpose; facts table; brand block with NeGot."""
    c.setFillColor(WHITE)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    _draw_img(c, LOGO, (W - 70) / 2, H - 50, w=70)
    _draw_img(c, NAME, (W - 210) / 2, H - 162, w=210)
    _draw_img(c, STRIP, (W - 360) / 2, H - 192, w=360)

    # hero
    hx, hw, htop, hh = LM + 6, W - 2 * LM - 12, H - 228, 196
    p = c.beginPath()
    p.roundRect(hx, htop - hh, hw, hh, 12)
    c.saveState()
    c.clipPath(p, stroke=0, fill=0)
    gradient_bar(c, hx, htop - hh, hw, hh)
    c.restoreState()
    c.setFillColor(WHITE)
    c.setFont("Calibri-Bold", 8.5)
    c.drawCentredString(W / 2, htop - 34, kicker or f"GenAI Architect Journey  ·  {folder}")
    size = 30 if pdfmetrics.stringWidth(title, "Calibri-Bold", 30) < hw - 40 else 23
    c.setFont("Calibri-Bold", size)
    c.drawCentredString(W / 2, htop - 86, title)
    c.setStrokeColor(WHITE)
    c.setLineWidth(1.6)
    c.line(W / 2 - 34, htop - 104, W / 2 + 34, htop - 104)
    sty = ParagraphStyle("sub", fontName="Calibri", fontSize=12.5, leading=16, textColor=WHITE,
                         alignment=1)
    para = Paragraph(subtitle, sty)
    pw, ph = para.wrap(hw - 70, 60)
    para.drawOn(c, (W - pw) / 2, htop - 124 - ph)

    # facts table
    y = htop - hh - 26
    rows = facts[:7]
    row_h = 21
    c.setFillColor(TINT)
    c.rect(LM, y - row_h * len(rows), W - 2 * LM, row_h * len(rows), stroke=0, fill=1)
    c.setFillColor(CORAL)
    c.rect(LM, y - row_h * len(rows), 2.4, row_h * len(rows), stroke=0, fill=1)
    for i, (k, v) in enumerate(rows):
        yy = y - row_h * i - 14
        c.setFont("Calibri-Bold", 8.6)
        c.setFillColor(BLUE)
        c.drawString(LM + 14, yy, k)
        c.setFont("Calibri", 8.6)
        c.setFillColor(INK)
        c.drawString(LM + 120, yy, v)
        if i:
            c.setStrokeColor(HAIR)
            c.setLineWidth(0.5)
            c.line(LM + 8, yy + 14, W - LM, yy + 14)

    # brand block
    gradient_bar(c, LM, 132, W - 2 * LM, 2.2)
    _draw_img(c, NEGOT, W / 2 - 150, 121, h=46)
    c.setFillColor(BLUE)
    c.setFont("Calibri-Bold", 12)
    c.drawString(W / 2 - 96, 104, BRAND)
    x = W / 2 - 96
    x += _link_text(c, WEBSITE_TEXT, x, 89, "Calibri", 9, MUTED, WEBSITE_URL)
    x += _link_text(c, "   ·   ", x, 89, "Calibri", 9, MUTED, None)
    _link_text(c, LINKEDIN_TEXT, x, 89, "Calibri", 9, MUTED, LINKEDIN_URL)
    draw_connect(c, 58)


def draw_connect(c, y, icon_h=11, size=7.3, gap=4, spacing=12):
    """'Connect' row: social logo + label for every official link, each one clickable.
    Logos come from zz-Brand-Assets/Social-Media-Logos/PNG; links without a logo are text."""
    from social import LINKS, logo_path
    items = []
    for l in LINKS:
        lp = logo_path(l)
        iw = 0
        if lp:
            w0, h0 = _img(lp).getSize()
            iw = icon_h * w0 / h0
        tw = pdfmetrics.stringWidth(l["label"], "Calibri", size)
        items.append((l, lp, iw, tw))
    lead_w = pdfmetrics.stringWidth("CONNECT", "Calibri-Bold", size) + spacing
    total = lead_w + sum(iw + (gap if iw else 0) + tw for _, _, iw, tw in items) + spacing * (len(items) - 1)
    x = (W - total) / 2
    c.setFont("Calibri-Bold", size)
    c.setFillColor(CORAL)
    c.drawString(x, y, "CONNECT")
    x += lead_w
    for l, lp, iw, tw in items:
        x0 = x
        if lp:
            c.drawImage(_img(lp), x, y - 2.5, width=iw, height=icon_h, mask="auto")
            x += iw + gap
        c.setFont("Calibri", size)
        c.setFillColor(BLUE)
        c.drawString(x, y, l["label"])
        x += tw
        c.linkURL(l["url"], (x0, y - 3, x, y + icon_h - 2), relative=0)
        x += spacing


# --------------------------------------------------------------------------- styles & blocks
S = {
    "h1": ParagraphStyle("h1", fontName="Calibri-Bold", fontSize=17, leading=21, textColor=BLUE,
                         spaceBefore=8, spaceAfter=2),
    "h2": ParagraphStyle("h2", fontName="Calibri-Bold", fontSize=12.5, leading=16, textColor=BLUE,
                         spaceBefore=9, spaceAfter=3),
    "lead": ParagraphStyle("lead", fontName="Calibri", fontSize=11.2, leading=15, textColor=CORAL,
                           spaceAfter=5),
    "p": ParagraphStyle("p", fontName="Calibri", fontSize=9.8, leading=13.6, textColor=INK,
                        spaceAfter=5, alignment=TA_LEFT),
    "li": ParagraphStyle("li", fontName="Calibri", fontSize=9.8, leading=13.2, textColor=INK,
                         leftIndent=13, bulletIndent=2, spaceAfter=2.2),
    "cell": ParagraphStyle("cell", fontName="Calibri", fontSize=8.8, leading=11.4, textColor=INK),
    "cellh": ParagraphStyle("cellh", fontName="Calibri-Bold", fontSize=8.8, leading=11.4,
                            textColor=WHITE),
    "code": ParagraphStyle("code", fontName="Consolas", fontSize=7.9, leading=10.2, textColor=BLUE),
    "callt": ParagraphStyle("callt", fontName="Calibri-Bold", fontSize=9.6, leading=12.5,
                            textColor=BLUE, spaceAfter=1),
    "small": ParagraphStyle("small", fontName="Calibri-Italic", fontSize=8.4, leading=11,
                            textColor=MUTED, spaceAfter=4),
}


def _md(text: str) -> str:
    """Tiny inline markup: **bold**, `code`, and & < > escaping."""
    import re
    t = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r'<font name="Consolas" color="#031273">\1</font>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return t


class _Rule(Spacer):
    def __init__(self, w=46, h=2.6):
        super().__init__(w, h + 6)
        self.rw, self.rh = w, h

    def draw(self):
        gradient_bar(self.canv, 0, 4, self.rw, self.rh)


def h1(text):
    return [CondPageBreak(150), Paragraph(_md(text), S["h1"]), _Rule()]


def h2(text):
    return [CondPageBreak(100), Paragraph(_md(text), S["h2"])]


def p(text):
    return Paragraph(_md(text), S["p"])


def lead(text):
    return Paragraph(_md(text), S["lead"])


def small(text):
    return Paragraph(_md(text), S["small"])


def bullets(items):
    return [Paragraph(_md(i), S["li"], bulletText="•") for i in items]


def table(header, rows, widths=None):
    avail = W - LM - RM
    n = len(header)
    widths = [avail * w for w in widths] if widths else [avail / n] * n
    data = [[Paragraph(_md(h), S["cellh"]) for h in header]]
    data += [[Paragraph(_md(str(v)), S["cell"]) for v in r] for r in rows]
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), BLUE),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LINEBELOW", (0, 1), (-1, -1), 0.5, HAIR),
             ("TOPPADDING", (0, 0), (-1, -1), 4.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
             ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), TINT))
    t.setStyle(TableStyle(style))
    return [t, Spacer(1, 7)]


def code(text, title=None):
    pre = Preformatted(text.strip("\n"), S["code"])
    rows = [[Paragraph(_md(title), S["callt"])]] if title else []
    rows.append([pre])
    t = Table(rows, colWidths=[W - LM - RM])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TINT),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.4, BLUE),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return [t, Spacer(1, 7)]


def callout(title, text, kind="note"):
    bg, bar = (CORAL_TINT, CORAL) if kind == "tip" else (TINT, BLUE)
    body = text if isinstance(text, list) else [text]
    cell = [Paragraph(_md(title), S["callt"])] + [Paragraph(_md(b), S["p"]) for b in body]
    t = Table([[cell]], colWidths=[W - LM - RM])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.6, bar),
                           ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return [KeepTogether([t]), Spacer(1, 7)]


def flow(steps):
    """Horizontal process boxes (coral → blue), e.g. Load → Split → Embed."""
    n = len(steps)
    avail = W - LM - RM
    gap = 10
    bw = (avail - gap * (n - 1)) / n
    sty = ParagraphStyle("fl", fontName="Calibri-Bold", fontSize=8.4, leading=10.4,
                         textColor=WHITE, alignment=1)
    cells, widths, style = [], [], [("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                     ("TOPPADDING", (0, 0), (-1, -1), 7),
                                     ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]
    arrow = ParagraphStyle("ar", fontName="Calibri-Bold", fontSize=11, textColor=BLUE, alignment=1)
    col = 0
    for i, s in enumerate(steps):
        cells.append(Paragraph(_md(s), sty))
        widths.append(bw - (gap if i < n - 1 else 0) * 0)
        style.append(("BACKGROUND", (col, 0), (col, 0), CORAL if i < (n + 1) // 2 else BLUE))
        col += 1
        if i < n - 1:
            cells.append(Paragraph("›", arrow))
            widths.append(gap)
            style.append(("LEFTPADDING", (col, 0), (col, 0), 0))
            style.append(("RIGHTPADDING", (col, 0), (col, 0), 0))
            col += 1
    scale = avail / sum(widths)
    t = Table([cells], colWidths=[w * scale for w in widths])
    t.setStyle(TableStyle(style))
    return [t, Spacer(1, 9)]


# --------------------------------------------------------------------------- document builder
class _NumberedCanvas(rl_canvas.Canvas):
    """Two-pass canvas so every footer can show 'PAGE n / N'."""

    def __init__(self, *a, meta=None, **kw):
        super().__init__(*a, **kw)
        self._saved = []
        self._meta = meta

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            count = getattr(self, "_annotationCount", 0)
            self.__dict__.update(state)
            # keep link-annotation names unique across the replayed pages
            self._annotationCount = max(count, getattr(self, "_annotationCount", 0))
            n = self._pageNumber
            m = self._meta
            if n == 1:
                draw_cover(self, m["folder"], m["title"], m["subtitle"], m["facts"], m.get("kicker"))
                if m.get("cover_extra"):
                    m["cover_extra"](self)          # optional per-document mark below the facts
            else:
                draw_header(self, m["folder"], m.get("short", m["title"]))
            draw_footer(self, f"PAGE {n} / {total}")
            super().showPage()
        super().save()


def build(out_path, *, folder, title, subtitle, facts, story, short=None, kicker=None,
          keywords="", cover_extra=None):
    """Render a branded explainer PDF. `story` is a list of flowables/lists from the helpers."""
    out_path = Path(out_path)
    meta = dict(folder=folder, title=title, subtitle=subtitle, facts=facts, short=short or title,
                kicker=kicker, cover_extra=cover_extra)
    doc = BaseDocTemplate(str(out_path), pagesize=A4, leftMargin=LM, rightMargin=RM,
                          topMargin=HEADER_BAND + 14, bottomMargin=FOOTER_BAND + 16,
                          title=title, author=BRAND, subject=folder, creator=BRAND,
                          keywords=keywords, producer="Shasu Vathanan brand PDF kit (ReportLab)")
    frame = Frame(LM, FOOTER_BAND + 16, W - LM - RM, H - HEADER_BAND - FOOTER_BAND - 30, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame])])
    flat = [PageBreak()]  # page 1 is the canvas-drawn cover
    for item in story:
        flat.extend(item if isinstance(item, list) else [item])
    doc.build(flat, canvasmaker=lambda *a, **kw: _NumberedCanvas(*a, meta=meta, **kw))
    return out_path
