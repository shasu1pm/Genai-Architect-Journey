<!-- brand:header:start -->
<p align="center">
  <img src="../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# Social-Media-Logos — Official Links and Platform Logos

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**The logos and links behind the Connect row that appears in every README, notebook, PDF cover, closing slide and web page footer of this repository.**

Every tool reads the list of links from [`../pdf-kit/social.py`](../pdf-kit/social.py) and the logo files from [`PNG/`](./PNG/). Change a link or a logo there, rerun the tools, and every file updates (see [`../pdf-kit/README.md`](../pdf-kit/README.md)).

---

## The eight official links

| # | Platform | Link | Logo used (`PNG/`) | Vector (`SVG/`) | Shortcut (`Source-Links/`) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | Website | [shasuvathanan.com](https://shasuvathanan.com) | <img src="PNG/website-personal-logo.png" alt="Website" height="28"> `website-personal-logo.png` | `website-personal-logo.svg` | `Personal-Website.url` |
| 2 | Email | [shasu1pm@gmail.com](mailto:shasu1pm@gmail.com) | <img src="PNG/Gmail_Logo.svg" alt="Email" height="22"> `Gmail_Logo.svg` | — (the logo itself is an SVG) | `Gmail-Email.txt` |
| 3 | LinkedIn | [linkedin.com/in/shasuvathanan](https://linkedin.com/in/shasuvathanan) | <img src="PNG/linkedin.png" alt="LinkedIn" height="24"> `linkedin.png` | `linkedin.svg` | `LinkedIn.url` |
| 4 | GitHub | [github.com/shasu1pm](https://github.com/shasu1pm) | <img src="PNG/github-custom.png" alt="GitHub" height="24"> `github-custom.png` | `github-custom.svg` | `GitHub-Profile.url` |
| 5 | Hugging Face | [huggingface.co/Shasuvathanan](https://huggingface.co/Shasuvathanan) | <img src="PNG/huggingface.png" alt="Hugging Face" height="24"> `huggingface.png` | `huggingface.svg` | `Hugging-Face.url` |
| 6 | YouTube | [youtube.com/@ShasuVathanan](https://www.youtube.com/@ShasuVathanan) | <img src="PNG/youtube.png" alt="YouTube" height="24"> `youtube.png` | `youtube.svg` | `YouTube.url` |
| 7 | X (Twitter) | [x.com/shasuvathanan](https://x.com/shasuvathanan) | <img src="PNG/x.png" alt="X" height="24"> `x.png` | `x.svg` | `X.url` |
| 8 | Higgsfield AI | [higgsfield.ai/@shasuvathanan](https://higgsfield.ai/@shasuvathanan) | <img src="PNG/Higgsfield_AI.png" alt="Higgsfield AI" height="24"> `Higgsfield_AI.png` | — | `Higgsfield.url` |

---

## Folder contents

```text
Social-Media-Logos/
├── README.md          ← this guide
├── README.txt         ← original package note (kept)
├── CREDITS.txt        ← where each logo came from
├── PNG/               ← the logos the tools use (Gmail_Logo is an SVG kept here on purpose)
├── SVG/               ← vector versions for design work (website and GitHub SVGs wrap the original PNGs)
└── Source-Links/      ← one shortcut or text file per official link
```

## Where the logos appear

| Place | How | Tool |
| :-- | :-- | :-- |
| README / `.md` footers | Row of linked logos + text links | `pdf-kit/apply_brand_markdown.py` |
| Notebook footer cells | Same row inside the last cell | `pdf-kit/apply_brand_markdown.py` |
| PDF covers | Clickable **CONNECT** row in the brand block | `pdf-kit/brand_pdf.py` (`draw_connect`) |
| Phase-005 closing slide | White panel of linked logos under CONNECT | `pdf-kit/brand_pptx_social.py` |
| Transformer Explorer web page | Connect row of logo buttons in the footer | `pdf-kit/brand_web_social.py` |

## Usage rules

- Use the files as they are — no copies in other folders, no recolouring. Tools downscale or render (SVG) **in memory** only.
- Keep the order in `social.py`; it is the display order everywhere.
- Platform logos stay on a white or light background (the closing slide uses a white panel for this reason).
- **Provenance:** the website and GitHub logos are the owner's own images; Hugging Face, LinkedIn, YouTube, X, Gmail and Higgsfield AI logos are trademarks of their respective owners, used only to link to the owner's profiles. The LinkedIn, X and YouTube SVGs carry their Font Awesome Free attribution comment (icons licensed CC BY 4.0) — keep it.

## Navigation

| Up | Index | Tools |
| :-- | :--: | --: |
| [zz-Brand-Assets](../) | [Journey index](../../README.md) | [pdf-kit →](../pdf-kit/) |

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
