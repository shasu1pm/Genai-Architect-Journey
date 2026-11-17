"""Official links and social profiles — the single source of truth for every brand tool.

Logos come from `zz-Brand-Assets/Social-Media-Logos/PNG/` and are used as they are.
Every link now has a logo (Email uses Gmail_Logo.svg, rendered in memory where a raster image
is needed). To add a platform, append an entry below and rerun the tools.
"""
from __future__ import annotations

from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1]
LOGO_DIR = ASSETS / "Social-Media-Logos" / "PNG"
LOGO_REL = "zz-Brand-Assets/Social-Media-Logos/PNG"   # repository-relative, for Markdown/HTML

# order = display order
LINKS = [
    dict(key="website", label="Website", text="shasuvathanan.com", url="https://shasuvathanan.com",
         logo="website-personal-logo.png"),
    dict(key="email", label="Email", text="shasu1pm@gmail.com", url="mailto:shasu1pm@gmail.com",
         logo="Gmail_Logo.svg"),
    dict(key="linkedin", label="LinkedIn", text="linkedin.com/in/shasuvathanan",
         url="https://linkedin.com/in/shasuvathanan", logo="linkedin.png"),
    dict(key="github", label="GitHub", text="github.com/shasu1pm", url="https://github.com/shasu1pm",
         logo="github-custom.png"),
    dict(key="huggingface", label="Hugging Face", text="huggingface.co/Shasuvathanan",
         url="https://huggingface.co/Shasuvathanan", logo="huggingface.png"),
    dict(key="youtube", label="YouTube", text="youtube.com/@ShasuVathanan",
         url="https://www.youtube.com/@ShasuVathanan", logo="youtube.png"),
    dict(key="x", label="X (Twitter)", text="x.com/shasuvathanan", url="https://x.com/shasuvathanan",
         logo="x.png"),
    dict(key="higgsfield", label="Higgsfield AI", text="higgsfield.ai/@shasuvathanan",
         url="https://higgsfield.ai/@shasuvathanan", logo="Higgsfield_AI.png"),
]


def open_logo(path, px=256):
    """Open a logo as a PIL RGBA image. SVG files (e.g. Gmail_Logo.svg) are rendered in memory
    with PyMuPDF so PDF, PowerPoint and web tools can use them; nothing is written to disk."""
    from PIL import Image
    path = Path(path)
    if path.suffix.lower() == ".svg":
        import io
        import fitz
        doc = fitz.open(str(path))
        page = doc[0]
        zoom = px / max(page.rect.width, page.rect.height)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True)
        return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGBA")
    return Image.open(path).convert("RGBA")


def logo_path(link):
    if not link["logo"]:
        return None
    p = LOGO_DIR / link["logo"]
    return p if p.exists() else None


def markdown_row(prefix: str) -> str:
    """HTML block for README/Markdown footers. `prefix` is the '../' depth to the repo root."""
    icons = []
    for l in LINKS:
        if logo_path(l):
            src = f"{prefix}{LOGO_REL}/{l['logo']}"
            icons.append(f'  <a href="{l["url"]}"><img src="{src}" alt="{l["label"]}" title="{l["label"]}" height="24"></a>')
    texts = " &nbsp;&#8226;&nbsp; ".join(f'<a href="{l["url"]}">{l["label"]}</a>' for l in LINKS)
    return ("<!-- brand:social:start -->\n<p align=\"center\">\n" + "\n  &nbsp;\n".join(icons) +
            f"\n  <br>\n  <sub><b>Connect:</b> {texts}</sub>\n</p>\n<!-- brand:social:end -->")
