"""Rebuild Multimodal-Retriever-Concepts-and-Architecture.pdf with the repository brand engine.

The guide's text, tables and diagram labels are kept verbatim in this file. After building, the
script checks that every source word, every table cell and every diagram label is in the PDF.

Run (from any folder):
    python Phase-007-RAG-Introduction/docs/build_multimodal.py
    python Phase-007-RAG-Introduction/docs/build_multimodal.py --compare <reference.pdf>   # also compare with another copy

Needs reportlab, pymupdf and pillow, Windows fonts Calibri/Consolas, and the repository's
zz-Brand-Assets/pdf-kit/brand_pdf.py (imported read-only, never modified).
"""
import re
import sys
from collections import Counter
from pathlib import Path

PHASE = Path(__file__).resolve().parents[1]          # Phase-007-RAG-Introduction/
REPO = PHASE.parent                                    # repository root
sys.path.insert(0, str(REPO / "zz-Brand-Assets" / "pdf-kit"))
from brand_pdf import (BLUE, CORAL, HAIR, INK, LM, MUTED, RM, TINT, W, WHITE, KeepTogether, Paragraph,  # noqa: E402
                       ParagraphStyle, S, Spacer, build, h1, h2, p, small)
from reportlab.lib import colors  # noqa: E402
from reportlab.platypus import Flowable, Table, TableStyle  # noqa: E402

FOLDER = "Phase-007-RAG-Introduction"
OUT = PHASE / "Multimodal-Retriever-Concepts-and-Architecture.pdf"
CORAL_TINT = colors.HexColor("#FFF1F3")
AVAIL = W - LM - RM


SOURCE: list[str] = []          # every text block placed in the document, for the self-check


def para(text):
    """Paragraph with a bold lead-in label such as 'Example:' (wording unchanged)."""
    SOURCE.append(text)
    m = re.match(r"^([A-Z][A-Za-z ]{2,30}:)(\s.*)$", text)
    esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return Paragraph(f"<b>{esc(m.group(1))}</b>{esc(m.group(2))}" if m else esc(text), S["p"])


def note(text):
    """Small note under a table (wording unchanged)."""
    SOURCE.append(text)
    sty = ParagraphStyle("note", parent=S["p"], fontSize=8.6, leading=11.6, textColor=INK)
    m = re.match(r"^([A-Z][A-Za-z ]{2,30}:)(\s.*)$", text)
    return Paragraph(f"<b>{m.group(1)}</b>{m.group(2)}" if m else text, sty)


def table(header, rows, widths, links=None):
    """Brand-style table; `links` maps a cell text to a URL to make it clickable."""
    links = links or {}
    hsty = ParagraphStyle("th", parent=S["cellh"])
    csty = ParagraphStyle("td", parent=S["cell"])
    def cell(t):
        t2 = t.replace("&", "&amp;")
        if t in links:
            return Paragraph(f'<link href="{links[t]}" color="#031273"><u>{t2}</u></link>', csty)
        return Paragraph(t2, csty)
    data = [[Paragraph(h, hsty) for h in header]] + [[cell(c) for c in r] for r in rows]
    t = Table(data, colWidths=[AVAIL * w for w in widths], repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), BLUE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LINEBELOW", (0, 1), (-1, -1), 0.5, HAIR),
             ("TOPPADDING", (0, 0), (-1, -1), 4.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4.4),
             ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]
    style += [("BACKGROUND", (0, i), (-1, i), TINT) for i in range(2, len(data), 2)]
    t.setStyle(TableStyle(style))
    return [t, Spacer(1, 5)]


class ArchitectureDiagram(Flowable):
    """Sources → Ingest and process → Store and index → Retrieve and use → Results to LLM / apps."""

    def __init__(self, width):
        super().__init__()
        self.width, self.height = width, 292

    def box(self, x, y, w, h, title, sub, fill, stroke, text):
        c = self.canv
        c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(1)
        c.roundRect(x, y, w, h, 7, stroke=1, fill=1)
        c.setFillColor(text)
        c.setFont("Calibri-Bold", 10.5); c.drawCentredString(x + w / 2, y + h - 17, title)
        c.setFont("Calibri", 8.6); c.drawCentredString(x + w / 2, y + 9, sub)

    def arrow(self, x, y1, y2):
        c = self.canv
        c.setStrokeColor(CORAL); c.setFillColor(CORAL); c.setLineWidth(1.4)
        c.line(x, y1, x, y2 + 5)
        path = c.beginPath(); path.moveTo(x - 4, y2 + 6); path.lineTo(x + 4, y2 + 6); path.lineTo(x, y2); path.close()
        c.drawPath(path, fill=1, stroke=0)

    def draw(self):
        cx, bw = self.width * 0.42, 280
        x0 = cx - bw / 2
        sw, gap = 118, 13
        sx = cx - (3 * sw + 2 * gap) / 2
        for i, (title, sub) in enumerate([("Text / files", "TXT, PDF, DOCX"), ("Media", "Image, video, audio"),
                                          ("Sources", "Web, GitHub, code")]):
            x = sx + i * (sw + gap)
            self.box(x, 246, sw, 44, title, sub, TINT, BLUE, BLUE)
            self.arrow(x + sw / 2, 246, 214)
        self.box(x0, 166, bw, 46, "Ingest and process", "Parsing / OCR / speech transcription / frame extraction",
                 BLUE, BLUE, WHITE)
        self.arrow(cx, 166, 134)
        self.box(x0, 86, bw, 46, "Store and index", "Metadata + embeddings + persistent original assets",
                 TINT, BLUE, BLUE)
        self.arrow(cx, 86, 54)
        self.box(x0, 6, bw, 46, "Retrieve and use", "Keyword + semantic + multimodal search + reranking",
                 CORAL_TINT, CORAL, BLUE)
        c = self.canv
        c.setStrokeColor(MUTED); c.setLineWidth(1); c.setDash(3, 2)
        c.line(x0 + bw, 29, x0 + bw + 22, 29); c.setDash()
        c.setFillColor(MUTED); c.setFont("Calibri-Bold", 9)
        c.drawString(x0 + bw + 28, 26, "Results to LLM / apps")


TOOLS = {"LlamaIndex": "https://docs.llamaindex.ai/", "Qdrant": "https://qdrant.tech/documentation/",
         "BAAI BGE-M3": "https://huggingface.co/BAAI/bge-m3", "OpenCLIP": "https://github.com/mlfoundations/open_clip",
         "FFmpeg": "https://ffmpeg.org/", "Whisper": "https://github.com/openai/whisper",
         "Docling": "https://github.com/docling-project/docling"}

T_TYPES = (["Data type", "What can be found", "Typical processing / search"], [
    ["Text", "Words, sentences, concepts", "Keyword + semantic search"],
    ["PDF", "Text, tables, figures", "PDF parsing, layout analysis, OCR if scanned"],
    ["Word", "Headings, paragraphs, tables", "DOCX extraction + indexing"],
    ["Excel", "Cells, rows, tabular values", "Spreadsheet parsing + structured queries"],
    ["Images", "Objects, visual similarity, text", "Vision, OCR, image embeddings"],
    ["Videos", "Scenes, dialogue, timestamps", "Transcript + sampled frames + time metadata"],
    ["Audio", "Speech and audio segments", "Transcription + audio embeddings"],
    ["Code", "Functions, classes, files", "Keyword, AST/code-aware search"],
    ["Websites", "Pages, articles and links", "APIs / crawling + extraction"],
    ["GitHub", "Repository code and docs", "API / clone + code indexing"]])
T_TOOLS = (["Component", "Tool", "Role"], [
    ["Retrieval framework", "LlamaIndex", "Pipelines, data connectors, retrieval orchestration"],
    ["Vector database", "Qdrant", "Persistent vector index and similarity search"],
    ["Text embeddings", "BAAI BGE-M3", "Semantic embeddings for text"],
    ["Image embeddings", "OpenCLIP", "Text-image similarity / image search"],
    ["Video processing", "FFmpeg", "Frames, audio tracks, and clip extraction"],
    ["Speech transcription", "Whisper", "Speech-to-text with timestamps where supported"],
    ["Document extraction", "Docling", "Structured extraction from documents"],
    ["Original asset store", "Local disk / object store", "Save and serve original files"]])
T_METHODS = (["Method", "Best use", "Practical example"], [
    ["Keyword search", "Exact terms, IDs, filenames", "Find a function called load_config"],
    ["Semantic search", "Related meaning and paraphrases", "“autonomous agent” matches “goal-directed AI”"],
    ["Multimodal search", "Image, text, or audio/video matching", "Find frames showing a dashboard"],
    ["Metadata filtering", "Dates, types, projects, timestamps", "Videos uploaded in October"],
    ["Original asset retrieval", "Get source content, not just summaries", "Open original PDF or cut video clip"]])
T_TERMS = (["Term", "Meaning", "What happens after app restarts?"], [
    ["Storing", "Putting data in RAM, a file, or database.", "Depends on where and how it was saved."],
    ["Persisting", "Saving data durably on disk or another persistent storage service.",
     "Data generally remains available after restart."]])
STEPS = [("1. Identify sources", "List document, media, code and web sources. Define file formats, access rights, and search goals."),
         ("2. Ingest and extract", "Parse documents, transcribe speech, extract video frames, capture metadata, and preserve file identifiers."),
         ("3. Chunk and enrich", "Split long text logically. Attach page numbers, video timestamps, source IDs, and file paths."),
         ("4. Generate embeddings", "Select compatible embedding models for text and image or other modalities."),
         ("5. Persist the data", "Save text indexes and embeddings in durable storage; preserve original files separately."),
         ("6. Build hybrid retrieval", "Combine exact keyword search with semantic/vector search and metadata filters."),
         ("7. Rerank and resolve assets", "Rank matching passages or media. Use source IDs to fetch original files and clips."),
         ("8. Connect to applications", "Supply retrieved evidence to an LLM, assistant, analysis workflow, or media-processing pipeline."),
         ("9. Evaluate and maintain", "Test relevance and accuracy. Update changed files, handle deletes, restrict access, and back up data.")]


def story():
    s = []
    s += h1("Multimodal Retriever")
    s.append(Paragraph("Concepts, supported data types, architecture, tools, persistence, and implementation workflow", S["lead"]))
    s += h2("1. Retriever concepts: what it is and how it works")
    s.append(para("A retriever finds and fetches relevant information from an indexed collection or another source. In a "
                  "Retrieval-Augmented Generation (RAG) system, the retriever supplies evidence to an LLM so its answer can "
                  "use relevant external content."))
    s.append(para("Three distinct jobs: (1) ingestion and processing extract usable information, (2) indexing and storage make "
                  "it searchable, and (3) retrieval searches and fetches relevant results. A retriever alone does not "
                  "automatically understand, edit, or generate every media type."))
    s.append(para("Example: Search “find the explanation of Agentic AI” → match paragraphs and video transcript timestamps "
                  "→ return source text, file references, and matching media segments."))
    s += [KeepTogether(h2("2. Supported data types") + table(*T_TYPES, [0.18, 0.34, 0.48]))]
    s.append(note("Important: A search index may store extracted content and links to original files. Finding a video "
                  "timestamp does not automatically produce a video clip; a separate media tool must fetch or cut the original asset."))
    s += [KeepTogether(h2("3. Multimodal retrieval architecture") + [
        para("The same searchable system can combine words, documents, images, audio, and video by indexing each "
             "source with the right processing method. Searches can retrieve content and source references."),
        Spacer(1, 4), ArchitectureDiagram(AVAIL), Spacer(1, 8)])]
    s.append(para("Example workflow: A user asks for a section of an instructional video. The system searches the transcript "
                  "and indexed frames, finds the relevant timestamp, then uses the stored file path and FFmpeg to extract the "
                  "requested clip. The retrieved clip can then be passed to a downstream application."))
    s += [KeepTogether(h2("4. Recommended tools and roles") + table(*T_TOOLS, [0.27, 0.25, 0.48], links=TOOLS))]
    s.append(note("Tools have distinct functions; choosing a model does not guarantee end-to-end multimodal search. Review "
                  "each tool and model license, resource requirements, and deployment options."))
    s += [KeepTogether(h2("5. Multimodal RAG and hybrid retrieval") + [
        para("Multimodal RAG uses retrieved information from more than one modality to support answers or downstream "
             "tasks. A practical hybrid system combines different search approaches for better recall and precision.")]
        + table(*T_METHODS, [0.25, 0.37, 0.38]))]
    s.append(para("Recommended pattern: Query → choose search modes → retrieve candidates → filter and rerank → fetch "
                  "relevant text or original assets → provide results with source references. An LLM may then reason over "
                  "retrieved information; media generation needs separate models or tools."))
    s += [KeepTogether(h2("6. Storing vs. persisting: simple explanation") + table(*T_TERMS, [0.18, 0.45, 0.37]))]
    s.append(para("Without persistence: Index 100 PDFs in RAM → close the application → the in-memory index is lost."))
    s.append(para("With persistence: Index 100 PDFs into a persistent vector database → close and reopen → stored index "
                  "remains available (assuming storage is intact)."))
    s.append(para("Key distinction: “Storing” is a general term, not a synonym for temporary memory. A persistent database "
                  "is also a form of storage. For reliable retrieval, persist the index, metadata, and paths or copies of "
                  "original files."))
    s += h2("7. Implementation workflow: step by step")
    step_title = ParagraphStyle("st", parent=S["p"], fontName="Calibri-Bold", textColor=BLUE, spaceAfter=0)
    for title, body in STEPS:
        s.append(KeepTogether([Paragraph(title, step_title), para(body)]))
    s += [KeepTogether(h2("Practical checklist") + [
        para("A useful minimum viable system includes: a document parser; a transcription step for audio/video; a "
             "persistent index; storage for original assets; a retrieval API; source references; and tests verifying "
             "that searches still work after restarting the application.")])]
    s += [KeepTogether(h2("Final takeaway") + [
        para("Retrieval is finding and fetching relevant material. Storing is putting data somewhere. Persisting is "
             "keeping it available across application restarts. Multimodal RAG combines retrieval with an LLM or "
             "another downstream system to work across diverse information types.")])]
    return s


def words(t):
    return Counter(re.findall(r"[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*", t))


HEADINGS = ["Multimodal Retriever", "Concepts, supported data types, architecture, tools, persistence, and implementation workflow",
            "1. Retriever concepts: what it is and how it works", "2. Supported data types",
            "3. Multimodal retrieval architecture", "4. Recommended tools and roles",
            "5. Multimodal RAG and hybrid retrieval", "6. Storing vs. persisting: simple explanation",
            "7. Implementation workflow: step by step", "Practical checklist", "Final takeaway"]
LABELS = ["Text / files", "TXT, PDF, DOCX", "Media", "Image, video, audio", "Sources", "Web, GitHub, code",
          "Ingest and process", "Parsing / OCR / speech transcription / frame extraction", "Store and index",
          "Metadata + embeddings + persistent original assets", "Retrieve and use",
          "Keyword + semantic + multimodal search + reranking", "Results to LLM / apps"]


def main():
    import fitz
    SOURCE.clear()
    build(OUT, folder=FOLDER, title="Multimodal Retriever", short="Multimodal Retriever · Concepts & Architecture",
          subtitle="Concepts, supported data types, architecture, tools, persistence, and implementation workflow",
          facts=[("Document", "Concept guide"), ("Topic", "Multimodal retrieval and multimodal RAG"),
                 ("Contents", "7 sections · 4 tables · architecture diagram · practical checklist"),
                 ("Tools covered", "LlamaIndex · Qdrant · BGE-M3 · OpenCLIP · FFmpeg · Whisper · Docling"),
                 ("Folder", FOLDER)],
          story=story(), keywords="multimodal retrieval, RAG, retriever, vector database, embeddings, persistence")
    new = fitz.open(OUT)
    new_text = "\n".join(pg.get_text() for pg in new)
    nw = words(new_text)
    norm = lambda t: " ".join(t.split())
    flat = norm(new_text)
    cells = [c for hdr, rows in (T_TYPES, T_TOOLS, T_METHODS, T_TERMS) for c in hdr + [x for r in rows for x in r]]
    source = SOURCE + HEADINGS + LABELS + cells + [title for title, _ in STEPS]   # step bodies are already in SOURCE
    sw = sum((words(t) for t in source), Counter())
    problems = {
        "source words missing": {w: n - nw[w] for w, n in sw.items() if nw[w] < n},
        "table cells missing": [c for c in cells if norm(c) not in flat],
        "diagram labels missing": [l for l in LABELS if l not in flat],
        "tool links missing": [u for u in TOOLS.values() if u not in {l.get("uri") for pg in new for l in pg.get_links()}],
    }
    if "--compare" in sys.argv:
        ref = fitz.open(sys.argv[sys.argv.index("--compare") + 1])
        ref_text = re.sub(r"MULTIMODAL RETRIEVER\s+\|\s+CONCEPTS & ARCHITECTURE\s*\n\s*\d+\s*\n", "\n",
                          "\n".join(pg.get_text() for pg in ref))
        problems["reference words missing"] = {w: n - nw[w] for w, n in words(ref_text).items() if nw[w] < n}
    print(f"{new.page_count} pages -> {OUT.relative_to(REPO)} | {len(cells)} table cells, {len(LABELS)} diagram labels, "
          f"{len(TOOLS)} tool links checked")
    for name, value in problems.items():
        print(f"  {name}: {value or 'none'}")
    if any(problems.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
