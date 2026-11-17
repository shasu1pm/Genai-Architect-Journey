<!-- brand:header:start -->
<p align="center">
  <img src="../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# Playwright Automation

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

📘 **Explainer:** [Playwright-Automation-Explainer.pdf](./Playwright-Automation-Explainer.pdf) — this folder in a short, branded guide.


This folder introduces browser RPA with Python and Playwright and contains two complete browser-automation projects. Unlike coordinate-based desktop automation, Playwright locates page elements through the browser's document structure and can wait for navigation and dynamic content.

📄 **Project document:** [Playwright Automation.pdf](./Playwright%20Automation.pdf)

## Contents

| File or project | Purpose |
| --- | --- |
| `Playwright_basic.py` | Opens Google in headless Chromium, saves `google.png`, and closes the browser |
| `Playwright_Functionality.py` | Reference comments listing common Playwright capabilities; it does not execute automation |
| [SauceDemo Product Automation](./Playwright%20Automation%20Project/) | Extracts every demo-store product, captures screenshots, and writes Excel output |
| [WhatsApp Automation Bot](./Playwright%20Assignment/) | Runs a consent-based WhatsApp Web messaging and reporting workflow in Edge |

## Setup for the basic example

```powershell
cd "Playwright Automation"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install playwright
python -m playwright install chromium
```

Run it with:

```powershell
python Playwright_basic.py
```

Because the browser is headless, no window appears. A successful run creates `google.png` in the current working directory.

## Common Playwright concepts demonstrated

- Starting and closing browsers and contexts
- Headed and headless execution
- Page navigation and URL waits
- Locating page elements using stable attributes
- Filling inputs and clicking controls
- Extracting text and metadata
- Taking full-page screenshots
- Reusing a persistent browser profile
- Handling timeouts, dynamic content, and selector fallbacks
- Producing JSON and Excel automation reports

The two subprojects have different dependencies and operational risks. Follow the README in the selected project directory rather than installing every dependency globally.

## Troubleshooting

- If Chromium is missing, run `python -m playwright install chromium` in the active environment.
- If browser installation is restricted, ensure the terminal has permission to download and execute Playwright browsers.
- If a page element cannot be found, the target site's HTML may have changed; inspect and update the relevant locator.
- Use `PWDEBUG=1` before a command to open Playwright Inspector while developing, for example: `$env:PWDEBUG='1'; python script.py`.

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
