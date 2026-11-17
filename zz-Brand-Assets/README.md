<!-- brand:header:start -->
<p align="center">
  <img src="../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# zz-Brand-Assets — Brand Assets and Templates

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**The single home of the official brand assets — and the tools that apply them to every README, notebook, PDF and web page in this repository.**

📄 **Brand guide:** [Brand-Guidelines.pdf](./Brand-Guidelines.pdf) — the assets, palette and usage rules in a 3-page branded document.

---

## Brand assets (used as they are)

| File | Role | Size | Used in |
| :-- | :-- | :-- | :-- |
| [Dragon-Motivation-Logo.png](./Dragon-Motivation-Logo.png) | Personal emblem / logo | 1019 × 1510 px | README and notebook headers, PDF covers and page headers, web favicon |
| [SHASUVATHANAN-NAME.png](./SHASUVATHANAN-NAME.png) | Name lockup | 1863 × 199 px | Root README, PDF covers and page headers |
| [ShasuVathanan-GEN AI-Product-Manager.png](./ShasuVathanan-GEN%20AI-Product-Manager.png) | Brand strip | 2323 × 63 px | Every README header, PDF covers and page headers |
| [NeGot-My-AI-Avatar.png](./NeGot-My-AI-Avatar.png) | **NeGot** — my AI avatar | 1254 × 1254 px | README and notebook footers, PDF footers and cover brand block, web page footer |
| [SHASUVATHANAN-THE-ONE-NAME.png](./SHASUVATHANAN-THE-ONE-NAME.png) | Hero banner — "The One Name" | 1280 × 320 px | Root README, full width directly above the main title |

> [!IMPORTANT]
> These four files are the only copies in the repository. Reference them from this folder — never copy, rename, resize, redraw or recolour them. PDF and web tools downscale the images **in memory** while embedding, so documents stay light and the source files stay untouched.

---

## Templates and tools — `pdf-kit/`

| File | What it does | Run (from the repository root) |
| :-- | :-- | :-- |
| [`pdf-kit/brand_pdf.py`](./pdf-kit/brand_pdf.py) | The brand PDF engine — cover, page header, page footer, palette, fonts and content blocks (`h1`, `p`, `bullets`, `table`, `code`, `callout`, `flow`) | imported by the scripts below |
| [`pdf-kit/build_docs.py`](./pdf-kit/build_docs.py) | Builds the code-defined explainers (Phase-004, Streamlit Resources, Phase-006, Phase-007) and `Brand-Guidelines.pdf` | `python zz-Brand-Assets/pdf-kit/build_docs.py` |
| [`pdf-kit/build_explainers.py`](./pdf-kit/build_explainers.py) + [`pdf-kit/explainers/`](./pdf-kit/explainers/) | Builds one `<Folder-Base>-Explainer.pdf` per phase and sub-project folder from a short Markdown source per folder | `python zz-Brand-Assets/pdf-kit/build_explainers.py` |
| [`pdf-kit/apply_covers.py`](./pdf-kit/apply_covers.py) | Gives every rebuilt PDF the same brand cover as the explainers | `python zz-Brand-Assets/pdf-kit/apply_covers.py` |
| [`pdf-kit/rebrand_existing.py`](./pdf-kit/rebrand_existing.py) | Re-brands existing PDFs: replaces only the old header and footer bands, never the body pages; splits PDFs over 15 pages into parts | `python zz-Brand-Assets/pdf-kit/rebrand_existing.py` |
| [`pdf-kit/apply_brand_markdown.py`](./pdf-kit/apply_brand_markdown.py) | Adds the brand header/footer to every `.md` and the brand cells to every notebook; a second run changes nothing | `python zz-Brand-Assets/pdf-kit/apply_brand_markdown.py .` |

Requirements: Python 3.10+, `reportlab`, `pymupdf`, `pillow`; Windows fonts Calibri and Consolas.

---

## Official links and social logos — `Social-Media-Logos/`

| Platform | Link | Logo |
| :-- | :-- | :-- |
| Website | [shasuvathanan.com](https://shasuvathanan.com) | [`website-personal-logo.png`](./Social-Media-Logos/PNG/website-personal-logo.png) |
| Email | [shasu1pm@gmail.com](mailto:shasu1pm@gmail.com) | [`Gmail_Logo.svg`](./Social-Media-Logos/PNG/Gmail_Logo.svg) (vector; rendered in memory for PDFs, slides and the web page) |
| LinkedIn | [linkedin.com/in/shasuvathanan](https://linkedin.com/in/shasuvathanan) | [`linkedin.png`](./Social-Media-Logos/PNG/linkedin.png) |
| GitHub | [github.com/shasu1pm](https://github.com/shasu1pm) | [`github-custom.png`](./Social-Media-Logos/PNG/github-custom.png) |
| Hugging Face | [huggingface.co/Shasuvathanan](https://huggingface.co/Shasuvathanan) | [`huggingface.png`](./Social-Media-Logos/PNG/huggingface.png) |
| YouTube | [youtube.com/@ShasuVathanan](https://www.youtube.com/@ShasuVathanan) | [`youtube.png`](./Social-Media-Logos/PNG/youtube.png) |
| X (Twitter) | [x.com/shasuvathanan](https://x.com/shasuvathanan) | [`x.png`](./Social-Media-Logos/PNG/x.png) |
| Higgsfield AI | [higgsfield.ai/@shasuvathanan](https://higgsfield.ai/@shasuvathanan) | [`Higgsfield_AI.png`](./Social-Media-Logos/PNG/Higgsfield_AI.png) |

These appear as a **Connect** row in every README footer, every notebook footer, every PDF cover, the Phase-005 closing slide and the Transformer Explorer web page footer. The list is kept in one place, [`pdf-kit/social.py`](./pdf-kit/social.py). Every link now has a logo. To add or change one, update `Social-Media-Logos/PNG/` and its entry in `social.py`, then rerun the tools (Markdown and notebooks: `apply_brand_markdown.py`; PDFs: `build_docs.py`, `build_explainers.py`, `build_spotify_sample.py`, `apply_covers.py`; slides: `brand_pptx_social.py`; web page: `brand_web_social.py`).

---

## How to reference the assets

Compute the relative path from the page's depth below the repository root and encode spaces as `%20`.

| Page location | Example path |
| :-- | :-- |
| Root `README.md` | `zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png` |
| One folder down (`Phase-007-RAG-Introduction/README.md`) | `../zz-Brand-Assets/NeGot-My-AI-Avatar.png` |
| Two folders down (`Phase-006-LangChain-Ecosystem/Langchain-Components/…`) | `../../zz-Brand-Assets/Dragon-Motivation-Logo.png` |

**Brand colours:** Coral `#FF4A62` → `#FF5A45` (accents, rules, gradients) · Deep Blue `#031273` (headings, tables, emphasis) · Soft Blue `#F2F4FF` (callouts) · no black. The artwork is red on transparency, so place it on a white or light background, never on a coral fill.

**Links:** [SHASUVATHANAN.COM](https://shasuvathanan.com) · [LinkedIn](https://www.linkedin.com/in/shasuvathanan) · [GitHub](https://github.com/shasu1pm/Genai-Architect-Journey)

> [!NOTE]
> The full rules live in [`Master-My-GitHub-Branding-Instruction.md`](../Master-My-GitHub-Branding-Instruction.md).

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
  <a href="https://shasuvathanan.com"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/website-personal-logo.png" alt="Website" title="Website" height="24"></a>
  &nbsp;
  <a href="mailto:shasu1pm@gmail.com"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/Gmail_Logo.svg" alt="Email" title="Email" height="24"></a>
  &nbsp;
  <a href="https://linkedin.com/in/shasuvathanan"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/linkedin.png" alt="LinkedIn" title="LinkedIn" height="24"></a>
  &nbsp;
  <a href="https://github.com/shasu1pm"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/github-custom.png" alt="GitHub" title="GitHub" height="24"></a>
  &nbsp;
  <a href="https://huggingface.co/Shasuvathanan"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/huggingface.png" alt="Hugging Face" title="Hugging Face" height="24"></a>
  &nbsp;
  <a href="https://www.youtube.com/@ShasuVathanan"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/youtube.png" alt="YouTube" title="YouTube" height="24"></a>
  &nbsp;
  <a href="https://x.com/shasuvathanan"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/x.png" alt="X (Twitter)" title="X (Twitter)" height="24"></a>
  &nbsp;
  <a href="https://higgsfield.ai/@shasuvathanan"><img src="../zz-Brand-Assets/Social-Media-Logos/PNG/Higgsfield_AI.png" alt="Higgsfield AI" title="Higgsfield AI" height="24"></a>
  <br>
  <sub><b>Connect:</b> <a href="https://shasuvathanan.com">Website</a> &nbsp;&#8226;&nbsp; <a href="mailto:shasu1pm@gmail.com">Email</a> &nbsp;&#8226;&nbsp; <a href="https://linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm">GitHub</a> &nbsp;&#8226;&nbsp; <a href="https://huggingface.co/Shasuvathanan">Hugging Face</a> &nbsp;&#8226;&nbsp; <a href="https://www.youtube.com/@ShasuVathanan">YouTube</a> &nbsp;&#8226;&nbsp; <a href="https://x.com/shasuvathanan">X (Twitter)</a> &nbsp;&#8226;&nbsp; <a href="https://higgsfield.ai/@shasuvathanan">Higgsfield AI</a></sub>
</p>
<!-- brand:social:end -->
<p align="center">
  <img src="../zz-Brand-Assets/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>Shasu Vathanan - GEN AI - Product Manager</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; <a href="../README.md">Back to the journey index</a></sub>
</p>
<!-- brand:footer:end -->
