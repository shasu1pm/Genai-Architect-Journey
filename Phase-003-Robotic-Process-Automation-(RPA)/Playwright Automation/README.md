# Playwright Automation

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

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

<a href="https://shasuvathanan.com" target="_blank" rel="noopener">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank" rel="noopener">LinkedIn</a>
