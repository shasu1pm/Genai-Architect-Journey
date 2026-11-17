"""Add (or refresh) the Connect panel on a deck's closing slide.

A white rounded panel holds every logo from social.py (each one a hyperlink); links without a
logo are listed as text underneath. Shapes are named `Social-*`, so a rerun replaces them.
Logos are rendered in memory (SVG included) — nothing is copied into the deck folder.

Run:  python zz-Brand-Assets/pdf-kit/brand_pptx_social.py Phase-005-LLM-Foundations-and-Practical-Tools/LLM-Foundations-and-Practical-Tools.pptx
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import LINKS, logo_path, open_logo  # noqa: E402

REPO = Path(__file__).resolve().parents[2]


def main(rel, right=12.71, top=4.05, panel_w=4.9):
    path = REPO / rel
    prs = Presentation(str(path))
    slide = prs.slides[-1]
    for sh in [sh for sh in slide.shapes if sh.name.startswith("Social-")]:
        sh._element.getparent().remove(sh._element)

    icons = [l for l in LINKS if logo_path(l)]
    texts = [l for l in LINKS if not logo_path(l)]
    panel_h = 0.98 if texts else 0.56
    x0 = right - panel_w
    panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x0), Inches(top),
                                   Inches(panel_w), Inches(panel_h))
    panel.name = "Social-panel"
    panel.fill.solid()
    panel.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    panel.line.fill.background()
    panel.shadow.inherit = False
    panel.adjustments[0] = 0.18

    h, gap = 0.34, 0.16
    imgs = [open_logo(logo_path(l), 320) for l in icons]
    widths = [h * im.width / im.height for im in imgs]
    x = x0 + (panel_w - sum(widths) - gap * (len(widths) - 1)) / 2
    for l, im, w in zip(icons, imgs, widths):
        im.thumbnail((160, 160), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "PNG", optimize=True)
        buf.seek(0)
        pic = slide.shapes.add_picture(buf, Inches(x), Inches(top + 0.11), Inches(w), Inches(h))
        pic.name = "Social-" + l["key"]
        pic.click_action.hyperlink.address = l["url"]
        pic._element.nvPicPr.cNvPr.set("descr", f'{l["label"]}: {l["text"]}')
        x += w + gap

    if texts:
        tb = slide.shapes.add_textbox(Inches(x0), Inches(top + 0.52), Inches(panel_w), Inches(0.36))
        tb.name = "Social-text"
        para = tb.text_frame.paragraphs[0]
        para.alignment = PP_ALIGN.CENTER
        for i, l in enumerate(texts):
            if i:
                r = para.add_run()
                r.text = "   •   "
                r.font.size = Pt(10.5)
            r = para.add_run()
            r.text = f'{l["label"]}: {l["text"]}'
            r.font.size = Pt(10.5)
            r.hyperlink.address = l["url"]
    prs.save(str(path))
    print(f"Connect panel: {len(icons)} logos, {len(texts)} text links -> {rel}")


if __name__ == "__main__":
    main(sys.argv[1])
