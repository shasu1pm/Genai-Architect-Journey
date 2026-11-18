"""Editable SVG sources for the project's diagrams (written by code, so they stay consistent).

- assets/comparison.svg   — LangChain vs LangGraph vs LangSmith infographic (with brand images)
- assets/architecture.svg — high-level system architecture
- assets/workflow.svg     — end-to-end LangGraph workflow with conditional routing

Brand colours: coral #FF4A62 → #FF5A45, deep blue #031273, tint #F2F4FF, ink #1B2559,
muted #5A6391 — never black. Brand images are referenced from zz-Brand-Assets as they are.
"""
from __future__ import annotations

from html import escape

CORAL, CORAL2, BLUE, TINT, INK, MUTED, HAIR = "#FF4A62", "#FF5A45", "#031273", "#F2F4FF", "#1B2559", "#5A6391", "#DDE1F2"
FONT = "Segoe UI, Helvetica, Arial, sans-serif"
ASSETS_FROM_SVG = "../../../zz-Brand-Assets/"          # assets/ → track → Phase-006 → repository root


def wrap(text: str, width_px: float, size: float) -> list[str]:
    """Greedy word wrap using an average glyph width (good enough for Segoe UI)."""
    max_chars = max(8, int(width_px / (size * 0.52)))
    lines, line = [], ""
    for word in text.split():
        if len(line) + len(word) + (1 if line else 0) > max_chars:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    return lines + ([line] if line else [])


class Svg:
    def __init__(self, width: int, height: int, title: str):
        self.w, self.h = width, height
        self.parts = ['<rect width="100%" height="100%" fill="#FFFFFF"/>']
        self.title = title

    def rect(self, x, y, w, h, fill, stroke=None, rx=14, sw=1.5, dash=None):
        s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{d}/>')

    def text(self, x, y, lines, size=16, weight=400, fill=INK, anchor="start", lh=1.35, spacing=None):
        if isinstance(lines, str):
            lines = [lines]
        ls = f' letter-spacing="{spacing}"' if spacing else ""
        spans = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else size * lh:.1f}">{escape(t)}</tspan>'
                        for i, t in enumerate(lines))
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
                          f'fill="{fill}" text-anchor="{anchor}"{ls}>{spans}</text>')
        return y + size * lh * (len(lines) - 1)

    def para(self, x, y, text, width, size=16, **kw):
        return self.text(x, y, wrap(text, width, size), size=size, **kw)

    def arrow(self, points, color=BLUE, dash=None, width=2.4):
        d = " ".join(f"{'M' if i == 0 else 'L'} {px} {py}" for i, (px, py) in enumerate(points))
        da = f' stroke-dasharray="{dash}"' if dash else ""
        marker = "arrow-coral" if color == CORAL else "arrow-blue"
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da} '
                          f'marker-end="url(#{marker})"/>')

    def diamond(self, cx, cy, w, h, label, fill=TINT, stroke=CORAL):
        pts = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
        self.parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2" stroke-dasharray="6 4"/>')
        self.text(cx, cy + 5, label, size=14, weight=700, fill=BLUE, anchor="middle")

    def image(self, href, x, y, w, h, alt):
        self.parts.append(f'<image href="{href}" x="{x}" y="{y}" width="{w}" height="{h}" '
                          f'preserveAspectRatio="xMidYMid meet"><title>{escape(alt)}</title></image>')

    def svg(self) -> str:
        defs = (f'<defs><linearGradient id="coral" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CORAL}"/>'
                f'<stop offset="1" stop-color="{CORAL2}"/></linearGradient>'
                f'<marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
                f'<path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>'
                f'<marker id="arrow-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
                f'<path d="M0,0 L10,5 L0,10 z" fill="{CORAL}"/></marker></defs>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{escape(self.title)}">'
                f'<title>{escape(self.title)}</title>{defs}{"".join(self.parts)}</svg>\n')


def node(s: Svg, cx, cy, label, kind="python", w=176, h=58, sub=None):
    """A workflow/architecture box. kind: chain (coral), python (blue), soft (tint), pill (start/end)."""
    x, y = cx - w / 2, cy - h / 2
    if kind == "chain":
        s.rect(x, y, w, h, "url(#coral)", rx=12)
        color = "#FFFFFF"
    elif kind == "python":
        s.rect(x, y, w, h, BLUE, rx=12)
        color = "#FFFFFF"
    elif kind == "pill":
        s.rect(x, y, w, h, "#FFFFFF", BLUE, rx=h / 2, sw=2.4)
        color = BLUE
    else:
        s.rect(x, y, w, h, TINT, BLUE, rx=12, sw=1.5)
        color = BLUE
    if sub:
        s.text(cx, cy - 3, label, size=16, weight=700, fill=color, anchor="middle")
        s.text(cx, cy + 16, sub, size=12, fill=color, anchor="middle")
    else:
        s.text(cx, cy + 6, label, size=16, weight=700, fill=color, anchor="middle")


def brand_footer(s: Svg, y: int, statement: str):
    s.parts.append(f'<line x1="60" y1="{y}" x2="{s.w - 60}" y2="{y}" stroke="{HAIR}" stroke-width="1.5"/>')
    s.image(ASSETS_FROM_SVG + "NeGot-My-AI-Avatar.png", 60, y + 16, 64, 64, "NeGot - my AI avatar")
    s.text(138, y + 44, "Shasu Vathanan - GEN AI - Product Manager", size=18, weight=800, fill=BLUE)
    s.text(138, y + 68, "SHASUVATHANAN.COM  ·  linkedin.com/in/shasuvathanan", size=14, weight=700, fill=CORAL, spacing="0.5")
    s.para(s.w - 60, y + 36, statement, 640, size=13, fill=MUTED, anchor="end")


# ----------------------------------------------------------------------------- 1. comparison infographic
def comparison_svg() -> str:
    s = Svg(1600, 2000, "LangChain vs LangGraph vs LangSmith — with FastAPI and Python")  # height set at the end
    # header
    s.image(ASSETS_FROM_SVG + "Dragon-Motivation-Logo.png", 60, 44, 72, 106, "Dragon Motivation logo")
    s.image(ASSETS_FROM_SVG + "SHASUVATHANAN-NAME.png", 150, 62, 420, 45, "SHASU VATHANAN")
    s.image(ASSETS_FROM_SVG + "ShasuVathanan-GEN%20AI-Product-Manager.png", 150, 122, 560, 15,
            "Shasu Vathanan - GEN AI - Product Manager")
    s.text(1540, 80, "Phase-006-LangChain-Ecosystem", size=18, weight=800, fill=BLUE, anchor="end")
    s.text(1540, 108, "AI Learning Assistant · GenAI Architect Journey", size=15, fill=MUTED, anchor="end")
    s.text(1540, 136, "SHASUVATHANAN.COM", size=15, weight=800, fill=CORAL, anchor="end", spacing="1")
    s.rect(60, 176, 1480, 6, "url(#coral)", rx=3)
    # title
    s.parts.append(f'<text x="60" y="262" font-family="{FONT}" font-size="56" font-weight="800" fill="{BLUE}">LangChain '
                   f'<tspan fill="{CORAL}">vs</tspan> LangGraph <tspan fill="{CORAL}">vs</tspan> LangSmith</text>')
    s.text(60, 306, "Build · Orchestrate · Observe — and how FastAPI and Python bring them together", size=24, fill=MUTED)

    cols = [
        ("LangChain", "BUILD", "chain",
         "An open-source framework for building applications with language models.",
         "Chat models · prompt templates · output parsers · tools · retrievers · LCEL chains",
         "One or a few model calls with clear inputs and outputs: Q&A, summaries, extraction.",
         "/ask — prompt template → chat model → Pydantic output parser"),
        ("LangGraph", "ORCHESTRATE", "python",
         "An open-source framework for stateful, multi-step AI workflows built as graphs.",
         "State · nodes · edges · conditional routing · loops with limits · human-in-the-loop",
         "The order of steps matters: branching, retries, approvals, long-running state.",
         "/workflow — classify → explain → add example → validate → retry or fallback"),
        ("LangSmith", "OBSERVE", "soft",
         "A hosted platform to trace, debug, monitor and evaluate LLM applications.",
         "Traces · run trees · latency and token metrics · datasets · evaluators · experiments",
         "Worth adding to any LLM app: see why an answer happened, find slow steps, test changes.",
         "Optional tracing from .env; each workflow run returns a trace_id"),
    ]
    labels = ["WHAT IT IS", "KEY BUILDING BLOCKS", "USE IT WHEN", "IN THIS PROJECT"]
    cw, gap, top, size, lh = 470, 35, 350, 20, 1.4
    wrapped = [[wrap(body, cw - 64, size) for body in col[3:]] for col in cols]
    row_heights = [34 + max(len(w[r]) for w in wrapped) * size * lh + 40 for r in range(len(labels))]
    card_h = 150 + 60 + sum(row_heights) + 10
    for i, (name, verb, kind, *rows) in enumerate(cols):
        x = 60 + i * (cw + gap)
        s.rect(x, top, cw, card_h, TINT if kind != "soft" else "#FFFFFF", CORAL if kind == "soft" else None, rx=20, sw=2.5)
        head_fill = "url(#coral)" if kind == "chain" else (BLUE if kind == "python" else "#FFF1F3")
        s.rect(x, top, cw, 150, head_fill, rx=20)
        s.rect(x + (1.25 if kind == "soft" else 0), top + 120, cw - (2.5 if kind == "soft" else 0), 30, head_fill, rx=0)
        head_text = "#FFFFFF" if kind != "soft" else BLUE
        s.text(x + 32, top + 52, verb, size=18, weight=800, fill=head_text if kind != "soft" else CORAL, spacing="3")
        s.text(x + 32, top + 112, name, size=46, weight=800, fill=head_text)
        y = top + 210
        for r, label in enumerate(labels):
            s.text(x + 32, y, label, size=15, weight=800, fill=CORAL, spacing="2")
            s.text(x + 32, y + 34, wrapped[i][r], size=size, fill=INK, lh=lh)
            y += row_heights[r]
    # FastAPI and Python bars
    y = top + card_h + 40
    s.rect(60, y, 1480, 110, "#FFFFFF", CORAL, rx=18, sw=2.5)
    s.text(96, y + 48, "SERVE", size=16, weight=800, fill=CORAL, spacing="3")
    s.text(96, y + 84, "FastAPI", size=34, weight=800, fill=BLUE)
    s.para(330, y + 50, "Exposes the assistant over HTTP: Pydantic request validation, consistent error codes, "
           "request logging and interactive Swagger UI at /docs.", 1170, size=20, fill=INK)
    y += 135
    s.rect(60, y, 1480, 110, BLUE, rx=18)
    s.text(96, y + 48, "IMPLEMENT", size=16, weight=800, fill="#FFB3BE", spacing="3")
    s.text(96, y + 84, "Python", size=34, weight=800, fill="#FFFFFF")
    s.para(330, y + 50, "Runs everything: configuration, safe logging, the LangChain chains, the LangGraph workflow, "
           "the FastAPI app and the pytest test suite.", 1170, size=20, fill="#FFFFFF")
    # how they relate
    y += 175
    s.text(60, y, "How they relate", size=30, weight=800, fill=BLUE)
    facts = [
        "Independent, not a required sequence: LangGraph can orchestrate any Python code, with or without LangChain inside its nodes.",
        "Complementary: LangChain components plug into LangGraph nodes when they are useful — as in this project.",
        "LangSmith only observes and evaluates. It is optional; the application runs the same without it.",
    ]
    y += 30
    for fact in facts:
        s.rect(60, y, 8, 52, "url(#coral)", rx=4)
        end = s.para(90, y + 32, fact, 1420, size=20, fill=INK)
        y = end + 46
    y += 6
    s.h = int(y + 120)
    brand_footer(s, y, "Independently designed and maintained by Shasu Vathanan.")
    return s.svg()


# ----------------------------------------------------------------------------- 2. architecture
def architecture_svg() -> str:
    s = Svg(1600, 980, "AI Learning Assistant — system architecture")
    s.text(60, 70, "System architecture — AI Learning Assistant", size=34, weight=800, fill=BLUE)
    s.text(60, 106, "How a question travels through FastAPI, LangChain, LangGraph and an optional LangSmith trace",
           size=18, fill=MUTED)
    s.rect(60, 128, 1480, 5, "url(#coral)", rx=2)

    def box(x, y, w, h, title, lines, kind, file=None):
        fill = {"chain": "url(#coral)", "python": BLUE, "soft": TINT, "dashed": "#FFFFFF"}[kind]
        stroke = {"soft": BLUE, "dashed": CORAL}.get(kind)
        s.rect(x, y, w, h, fill, stroke, rx=16, sw=2.2, dash="9 6" if kind == "dashed" else None)
        light = kind in ("chain", "python")
        s.text(x + 24, y + 40, title, size=22, weight=800, fill="#FFFFFF" if light else BLUE)
        if file:
            s.text(x + w - 24, y + 40, file, size=14, weight=700, fill="#FFE1E6" if light else CORAL, anchor="end")
        yy = y + 74
        for line in lines:
            yy = s.para(x + 24, yy, line, w - 48, size=16, fill="#FFFFFF" if light else INK) + 26

    box(60, 190, 300, 200, "Client", ["Swagger UI at /docs", "curl or Postman", "examples/sample_requests.py"], "soft")
    box(440, 190, 380, 200, "FastAPI", ["Pydantic validation (422)", "Error handling (502 · 503)",
                                         "Request logging, no secrets", "/health · /ask · /workflow"], "python", "app/main.py")
    box(920, 170, 600, 150, "LangChain — /ask", ["Prompt template → chat model → Pydantic output parser",
                                                  "One call, one structured answer"], "chain", "app/chains.py")
    box(920, 360, 600, 170, "LangGraph — /workflow", ["StateGraph: receive → classify → explain → add_example → "
                                                       "validate → retry or fallback → finalize"], "python", "app/graph.py")
    box(920, 580, 600, 150, "Chat model provider", ["Mock (default, offline, labelled) · OpenAI · Ollama (local)",
                                                     "Chosen by LLM_PROVIDER"], "soft", "app/llm.py")
    box(440, 580, 380, 150, "LangSmith", ["Optional: traces, latency, errors,",
                                           "evaluations — only when enabled"], "dashed", "app/observability.py")
    box(60, 580, 300, 150, "Configuration", [".env → LLM_PROVIDER, keys, retries, tracing"], "soft", "app/config.py")

    s.arrow([(360, 270), (436, 270)])
    s.text(398, 258, "HTTP", size=13, weight=700, fill=MUTED, anchor="middle")
    s.arrow([(820, 230), (916, 230)])
    s.text(868, 218, "/ask", size=14, weight=700, fill=BLUE, anchor="middle")
    s.arrow([(820, 340), (870, 340), (870, 445), (916, 445)])
    s.text(868, 328, "/workflow", size=14, weight=700, fill=BLUE, anchor="middle")
    s.arrow([(1490, 360), (1490, 324)], color=CORAL)
    s.text(1480, 350, "nodes call chains", size=13, weight=700, fill=CORAL, anchor="end")
    s.arrow([(1520, 245), (1560, 245), (1560, 655), (1524, 655)])
    s.arrow([(1220, 530), (1220, 576)])
    s.text(1232, 560, "model calls", size=13, weight=700, fill=MUTED)
    s.arrow([(630, 390), (630, 576)], color=CORAL, dash="7 5")
    s.text(642, 470, "traces of /ask and", size=13, weight=700, fill=CORAL)
    s.text(642, 488, "/workflow runs (optional)", size=13, weight=700, fill=CORAL)
    s.arrow([(360, 655), (436, 655)], dash="4 4")
    s.text(398, 643, "settings", size=13, weight=700, fill=MUTED, anchor="middle")

    s.rect(60, 780, 1480, 92, BLUE, rx=16)
    s.text(96, 822, "Python 3.10+", size=22, weight=800, fill="#FFFFFF")
    s.text(96, 852, "runs every layer", size=15, fill="#FFB3BE")
    s.para(330, 824, "Reusable modules in app/ · type hints and Pydantic models · logging with secret redaction · "
           "automated pytest tests", 1180, size=18, fill="#FFFFFF")
    s.text(60, 930, "Coral = LangChain · Deep blue = LangGraph, FastAPI and plain Python · Dashed = optional",
           size=15, fill=MUTED)
    s.text(1540, 930, "Shasu Vathanan - GEN AI - Product Manager · SHASUVATHANAN.COM", size=15, weight=700,
           fill=CORAL, anchor="end")
    return s.svg()


# ----------------------------------------------------------------------------- 3. workflow
def workflow_svg() -> str:
    s = Svg(1600, 900, "AI Learning Assistant — LangGraph workflow with conditional routing")
    s.text(60, 70, "LangGraph workflow — end to end", size=34, weight=800, fill=BLUE)
    s.text(60, 106, "POST /workflow · conditional routing · bounded retry · fallback · always reaches END",
           size=18, fill=MUTED)
    s.rect(60, 128, 1480, 5, "url(#coral)", rx=2)

    y1, y2, y3, y4 = 220, 430, 620, 770
    node(s, 115, y1, "START", "pill", w=100, h=52)
    node(s, 280, y1, "receive", sub="init state")
    node(s, 480, y1, "classify", sub="topic · type")
    s.diamond(690, y1, 180, 104, "small talk?")
    node(s, 920, y1, "clarify", sub="ask for a question")
    node(s, 690, y2, "explain", "chain", sub="LangChain chain")
    node(s, 920, y2, "add_example", "chain", sub="LangChain chain")
    node(s, 1150, y2, "validate", sub="fields present?")
    node(s, 1370, y2, "finalize", sub="status · response")
    node(s, 1530, y2, "END", "pill", w=96, h=52)
    s.diamond(1150, y3, 180, 104, "valid?")
    node(s, 1150, y4, "fallback", sub="predefined answer")

    s.arrow([(165, y1), (188, y1)])
    s.arrow([(368, y1), (388, y1)])
    s.arrow([(568, y1), (598, y1)])
    s.arrow([(780, y1), (828, y1)])
    s.text(804, y1 - 14, "yes", size=14, weight=700, fill=BLUE, anchor="middle")
    s.arrow([(1008, y1), (1370, y1), (1370, y2 - 33)])
    s.arrow([(690, y1 + 52), (690, y2 - 33)])
    s.text(702, y1 + 112, "no — a learning question", size=14, weight=700, fill=BLUE)
    s.arrow([(778, y2), (828, y2)], color=CORAL)
    s.arrow([(1008, y2), (1058, y2)], color=CORAL)
    s.arrow([(1150, y2 + 29), (1150, y3 - 56)])
    s.arrow([(1458, y2), (1478, y2)])
    # valid → finalize
    s.arrow([(1240, y3), (1370, y3), (1370, y2 + 33)])
    s.text(1300, y3 - 12, "yes", size=14, weight=700, fill=BLUE, anchor="middle")
    # not valid, attempts left → retry explain
    s.arrow([(1060, y3), (690, y3), (690, y2 + 33)], color=CORAL, dash="8 6")
    s.text(875, y3 - 12, "no, attempts < max → retry", size=14, weight=700, fill=CORAL, anchor="middle")
    # not valid, attempts used up → fallback → finalize
    s.arrow([(1150, y3 + 52), (1150, y4 - 33)])
    s.text(1162, y3 + 92, "no, attempts used up", size=14, weight=700, fill=BLUE)
    s.arrow([(1238, y4), (1440, y4), (1440, y2 + 33)])

    s.rect(60, 850, 18, 18, "url(#coral)", rx=4)
    s.text(88, 865, "LangChain chain (model call)", size=15, fill=INK)
    s.rect(360, 850, 18, 18, BLUE, rx=4)
    s.text(388, 865, "Plain Python node", size=15, fill=INK)
    s.parts.append(f'<polygon points="609,850 618,859 609,868 600,859" fill="{TINT}" stroke="{CORAL}" stroke-width="2"/>')
    s.text(630, 865, "Conditional edge (Python routing function)", size=15, fill=INK)
    s.text(1540, 865, "Shasu Vathanan - GEN AI - Product Manager", size=15, weight=700, fill=CORAL, anchor="end")
    return s.svg()


SVGS = {"comparison.svg": comparison_svg, "architecture.svg": architecture_svg, "workflow.svg": workflow_svg}
