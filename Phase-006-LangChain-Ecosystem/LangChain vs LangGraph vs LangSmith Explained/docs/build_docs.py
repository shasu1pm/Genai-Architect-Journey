"""Build every documentation asset of this project.

    python docs/build_docs.py            SVG diagrams + infographic PNG + both PDFs
    python docs/build_docs.py --images   only the SVG diagrams and the infographic PNG

Outputs (all inside this project folder):
    assets/comparison.svg, assets/architecture.svg, assets/workflow.svg   editable sources
    LangChain vs LangGraph vs LangSmith Explained.png                      infographic (PNG of comparison.svg)
    docs/LangChain-LangGraph-LangSmith-Guide.pdf                           full guide
    LangChain-vs-LangGraph-vs-LangSmith-Explained-Explainer.pdf            short explainer

Needs Google Chrome (to render SVG to PNG) and the repository's brand PDF engine in
zz-Brand-Assets/pdf-kit (used read-only). Brand images are read as they are and only
downscaled in memory.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

DOCS = Path(__file__).resolve().parent
PROJECT = DOCS.parent
REPO = PROJECT.parents[1]
ASSETS = PROJECT / "assets"
INFOGRAPHIC = PROJECT / "LangChain vs LangGraph vs LangSmith Explained.png"
CHROME = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")

sys.path.insert(0, str(DOCS))
from diagrams import SVGS  # noqa: E402


def write_svgs() -> dict[str, Path]:
    ASSETS.mkdir(exist_ok=True)
    paths = {}
    for name, make in SVGS.items():
        path = ASSETS / name
        path.write_text(make(), encoding="utf-8")
        paths[name] = path
    return paths


def render_png(svg: Path, out: Path, scale: float = 2.0) -> Path:
    """Render an SVG with headless Chrome at `scale` × its own size."""
    import re
    from PIL import Image
    head = svg.read_text(encoding="utf-8")[:300]
    width, height = (int(v) for v in re.search(r'width="(\d+)" height="(\d+)"', head).groups())
    with tempfile.TemporaryDirectory() as tmp:
        shot = Path(tmp) / "shot.png"
        url = svg.as_uri().replace("#", "%23")
        subprocess.run([str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--allow-file-access-from-files", f"--window-size={width},{height}",
                        f"--force-device-scale-factor={scale}", f"--screenshot={shot}", url],
                       check=True, capture_output=True, timeout=120)
        Image.open(shot).convert("RGB").save(out, "PNG", optimize=True)
    return out


def build_images() -> dict[str, Path]:
    svgs = write_svgs()
    render_png(svgs["comparison.svg"], INFOGRAPHIC)
    for path in svgs.values():
        print(f"svg  {path.relative_to(PROJECT)}")
    print(f"png  {INFOGRAPHIC.name}")
    return svgs


if __name__ == "__main__":
    svgs = build_images()
    if "--images" not in sys.argv:
        from guide import build_pdfs
        build_pdfs(svgs, render_png)
