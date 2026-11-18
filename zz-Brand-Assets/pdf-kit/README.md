<!-- brand:header:start -->
<p align="center">
  <img src="../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# pdf-kit — The Brand Toolkit

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**The scripts that put the brand on every README, notebook, PDF, slide deck and web page in this repository — and keep them consistent.**

All artwork comes from [`zz-Brand-Assets/`](../) and [`Social-Media-Logos/`](../Social-Media-Logos/); the files there are never modified or copied — images are downscaled or rendered (SVG) **in memory** while embedding.

---

## Requirements

- Python 3.10+ with `reportlab`, `pymupdf`, `pillow`, `python-pptx`, `nbformat`
- Windows fonts **Calibri** and **Consolas** (`C:\Windows\Fonts`)
- Run every command from the **repository root**

## Run order after any brand change

```powershell
python zz-Brand-Assets/pdf-kit/apply_brand_markdown.py .                 # 1. README/.md header + footer (Connect row), notebook brand cells
python zz-Brand-Assets/pdf-kit/build_explainers.py                       # 2. explainer PDFs from explainers/*.md
python zz-Brand-Assets/pdf-kit/build_docs.py                             # 3. code-defined explainers + Brand-Guidelines.pdf
python zz-Brand-Assets/pdf-kit/build_spotify_sample.py                   # 4. Phase-007 RAG sample PDF
python zz-Brand-Assets/pdf-kit/build_catalog_sample.py                   # 4b. Phase-008 product catalogue (RAG agent input)
python zz-Brand-Assets/pdf-kit/apply_covers.py                           # 5. brand cover on every rebuilt content PDF and split part
python zz-Brand-Assets/pdf-kit/brand_pptx_social.py <deck.pptx>          # 6. Connect panel on a deck's closing slide
python zz-Brand-Assets/pdf-kit/brand_web_social.py <page.html>           # 7. Connect row in a bundled web page footer
```

`build_explainers.py` and `build_docs.py` accept name filters, for example `python zz-Brand-Assets/pdf-kit/build_explainers.py 07-`.

---

## The scripts

| Script | What it does | Safe to rerun |
| :-- | :-- | :-- |
| [`social.py`](./social.py) | The eight official links and their logos (display order, labels, URLs); `open_logo()` renders SVG logos in memory | — (data) |
| [`brand_pdf.py`](./brand_pdf.py) | PDF engine: cover (logo, name lockup, brand strip, coral hero, facts, NeGot brand block, **CONNECT** row), page header (exact folder name), footer (`PAGE n / N`), and content blocks `h1 h2 lead p bullets table code callout flow` | — (library) |
| [`apply_brand_markdown.py`](./apply_brand_markdown.py) | Adds the brand header to every `.md`, regenerates the managed footer (with the Connect row), adds brand cells to every notebook; never touches private branding-instruction files | ✅ second run changes 0 files |
| [`build_explainers.py`](./build_explainers.py) | Builds one `<Folder-Base>-Explainer.pdf` per folder from a short Markdown source in [`explainers/`](./explainers/) | ✅ |
| [`build_docs.py`](./build_docs.py) | Code-defined explainers (Phase-004, Streamlit Resources, Phase-006 and its two tracks, Phase-007) and [`Brand-Guidelines.pdf`](../Brand-Guidelines.pdf) | ✅ |
| [`build_spotify_sample.py`](./build_spotify_sample.py) | Rebuilds the Phase-007 RAG input PDF from its verbatim text in [`sources/`](./sources/) and checks every word survives | ✅ |
| [`build_catalog_sample.py`](./build_catalog_sample.py) | Rebuilds the Phase-008 `products_catalog.pdf` from its verbatim text in [`sources/`](./sources/); checks every word survives and that `rag.py` still splits it into one chunk per product | ✅ |
| [`apply_covers.py`](./apply_covers.py) | Redraws the brand cover on the 13 rebuilt content PDFs, refreshes the inserted covers (Phase-005 Part 1, Transformer Part 1) and the split-part covers | ✅ |
| [`rebrand_existing.py`](./rebrand_existing.py) | One-time migration for legacy PDFs: replaces only the old header/footer bands (body pages untouched, safety check aborts on overlap) and splits PDFs over 15 pages | ⚠️ only for a new legacy PDF |
| [`brand_pptx_social.py`](./brand_pptx_social.py) | Adds or refreshes the Connect panel (shapes named `Social-*`) on a deck's closing slide | ✅ |
| [`brand_web_social.py`](./brand_web_social.py) | Adds the Connect row to a bundled HTML page (logos embedded in its manifest) | ⚠️ skips if present — restore a pre-Connect backup to refresh |

---

## Explainer sources — `explainers/`

| Source | Builds |
| :-- | :-- |
| `01-Programming-Foundations.md` | `Phase-001-Programming-Foundations/Programming-Foundations-Explainer.pdf` |
| `02-GenAI-Python-Toolkit.md` | `Phase-002-GenAI-Python-Toolkit/GenAI-Python-Toolkit-Explainer.pdf` |
| `03-Robotic-Process-Automation.md` | `Phase-003-…/Robotic-Process-Automation-Explainer.pdf` |
| `04-PyAutoGUI-Automation.md` | `…/PyAutoGUI Automation/PyAutoGUI-Automation-Explainer.pdf` |
| `05-Bengaluru-Weather-Bot.md` | `…/Assignment-1-PyAutoGUI_Weather_Data/Bengaluru-Weather-Bot-Explainer.pdf` |
| `06-Apple-Stock-Price-Bot.md` | `…/Assignment-2-PyAutoGUI_Bot_Stock_Price/Apple-Stock-Price-Bot-Explainer.pdf` |
| `07-Playwright-Automation.md` | `…/Playwright Automation/Playwright-Automation-Explainer.pdf` |
| `08-WhatsApp-Automation-Bot.md` | `…/Playwright Assignment/WhatsApp-Automation-Bot-Explainer.pdf` |
| `09-SauceDemo-Product-Automation.md` | `…/Playwright Automation Project/SauceDemo-Product-Automation-Explainer.pdf` |
| `10-FirstAPI.md` | `Phase-004-…/FirstAPI/FirstAPI-Explainer.pdf` |
| `11-Basic-FastAPI-App.md` | `…/FirstAPI/FastAPI App Assignments/Basic-FastAPI-App-Explainer.pdf` |
| `12-Streamlit.md` | `…/Streamlit/Streamlit-Explainer.pdf` |
| `13-Student-Grade-App.md` | `…/Streamlit Assignment Details/Student-Grade-App-Explainer.pdf` |
| `14-LLM-Foundations-and-Practical-Tools.md` | `Phase-005-…/LLM-Foundations-and-Practical-Tools-Explainer.pdf` |
| `15-Transformer-Explorer.md` | `Transformer-Explorer-Guide/Transformer-Explorer-Explainer.pdf` |
| `16-RAG-Agent-Explained.md` | `Phase-008-RAG-Agent-Explained/RAG-Agent-Explained-Explainer.pdf` |
| — built inside the folder by its own `docs/build_docs.py` (no source here) | `Phase-006-…/LangChain vs LangGraph vs LangSmith Explained/LangChain-vs-LangGraph-vs-LangSmith-Explained-Explainer.pdf` |
| *(in `build_docs.py`)* | Phase-004, Streamlit Resources, Phase-006, LangChain Components, Advanced Model Integration and Phase-007 explainers, plus `Brand-Guidelines.pdf` |

### Explainer source format

~~~text
---
out: Phase-008-Example/Example-Explainer.pdf
folder: Phase-008-Example
title: Example
subtitle: One-line purpose shown on the cover
fact: Document | Phase explainer
fact: Folder | Phase-008-Example
---
# Heading 1                ## Heading 2
lead: one coloured lead sentence
flow: Step A > Step B > Step C
- bullet
| table | header |          (GitHub table; never put a pipe inside a cell)
```lang Optional title       (fenced code)
> [!NOTE] Title  /  > [!TIP] Title   followed by "> text" lines
_note: small italic note
any other line is a paragraph
~~~

Recommended structure (3–5 pages): What it is → Why it matters → What is in this folder → How it works → Run it → Expected output → contextual example where it helps (labelled) → Key takeaways.

## Other source files — `sources/`

| File | Purpose |
| :-- | :-- |
| `spotify_web_app_architecture.txt` | Verbatim text of the Phase-007 RAG sample document |
| `products_catalog.txt` | Verbatim text of the Phase-008 ShopEasy product catalogue (a hypothetical store) |
| `spotify-logo.png` | Spotify logo supplied by the owner (trademark of Spotify AB), used only on that sample with a non-affiliation notice — never part of the personal brand |

## Add a new folder

1. Write `explainers/NN-<Folder-Base>.md` from the folder's real README, notebooks and code.
2. Run steps 1, 2 and 5 of the run order (and 6/7 if the folder has a deck or web page).
3. Link the explainer from the folder README and the root README row; check that no PDF is over 15 pages.

## Navigation

| Up | Index | Logos |
| :-- | :--: | --: |
| [zz-Brand-Assets](../) | [Journey index](../../README.md) | [Social-Media-Logos →](../Social-Media-Logos/) |

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>

<!-- brand:footer:start -->
<!-- brand:social:start -->
<p align="center">
  <a href="https://shasuvathanan.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/website-personal-logo.png" alt="Website" title="Website" height="24"></a>
  &nbsp;
  <a href="mailto:shasu1pm@gmail.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Gmail_Logo.svg" alt="Email" title="Email" height="24"></a>
  &nbsp;
  <a href="https://linkedin.com/in/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/linkedin.png" alt="LinkedIn" title="LinkedIn" height="24"></a>
  &nbsp;
  <a href="https://github.com/shasu1pm"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/github-custom.png" alt="GitHub" title="GitHub" height="24"></a>
  &nbsp;
  <a href="https://huggingface.co/Shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/huggingface.png" alt="Hugging Face" title="Hugging Face" height="24"></a>
  &nbsp;
  <a href="https://www.youtube.com/@ShasuVathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/youtube.png" alt="YouTube" title="YouTube" height="24"></a>
  &nbsp;
  <a href="https://x.com/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/x.png" alt="X (Twitter)" title="X (Twitter)" height="24"></a>
  &nbsp;
  <a href="https://higgsfield.ai/@shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Higgsfield_AI.png" alt="Higgsfield AI" title="Higgsfield AI" height="24"></a>
  <br>
  <sub><b>Connect:</b> <a href="https://shasuvathanan.com">Website</a> &nbsp;&#8226;&nbsp; <a href="mailto:shasu1pm@gmail.com">Email</a> &nbsp;&#8226;&nbsp; <a href="https://linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm">GitHub</a> &nbsp;&#8226;&nbsp; <a href="https://huggingface.co/Shasuvathanan">Hugging Face</a> &nbsp;&#8226;&nbsp; <a href="https://www.youtube.com/@ShasuVathanan">YouTube</a> &nbsp;&#8226;&nbsp; <a href="https://x.com/shasuvathanan">X (Twitter)</a> &nbsp;&#8226;&nbsp; <a href="https://higgsfield.ai/@shasuvathanan">Higgsfield AI</a></sub>
</p>
<!-- brand:social:end -->
<p align="center">
  <img src="../../zz-Brand-Assets/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>Shasu Vathanan - GEN AI - Product Manager</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; <a href="../../README.md">Back to the journey index</a></sub>
</p>
<!-- brand:footer:end -->
