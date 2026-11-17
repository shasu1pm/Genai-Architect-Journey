---
out: Phase-003-Robotic-Process-Automation-(RPA)/Playwright Automation/Playwright-Automation-Explainer.pdf
folder: Phase-003-Robotic-Process-Automation-(RPA)
title: Playwright Automation
subtitle: Browser RPA — locating page elements through the document structure instead of screen coordinates
fact: Document | Sub-project explainer
fact: Level | Beginner to intermediate
fact: Contents | 2 learning scripts · 2 complete projects
fact: Tools | Python · Playwright · Chromium / Microsoft Edge
fact: Folder | Phase-003-Robotic-Process-Automation-(RPA)/Playwright Automation
keywords: Playwright, browser automation, selectors
---
# What it is
lead: Playwright controls a real browser through its automation API — it finds elements, waits for them, and acts on them.
Unlike coordinate-based desktop automation, Playwright locates page elements through the browser's document structure and can wait for navigation and dynamic content. That makes browser automations far more reliable than clicking at screen positions.

# What is in this folder
| File or project | Purpose |
| :-- | :-- |
| `Playwright_basic.py` | Opens Google in headless Chromium, saves `google.png`, closes the browser |
| `Playwright_Functionality.py` | Reference comments listing common Playwright capabilities (does not run automation) |
| `Playwright Automation Project/` | **SauceDemo Product Automation** — products, screenshots, Excel report |
| `Playwright Assignment/` | **WhatsApp Automation Bot** — consent-based messaging and reports in Edge |

# How a Playwright script flows
flow: Start Playwright > Launch browser > Open page > Locate + act > Extract / screenshot > Close
| Concept | What it means |
| :-- | :-- |
| Browser, context, page | The browser process, an isolated session, and one tab |
| Headed vs headless | A visible window, or none at all |
| Locators | Find elements by stable attributes such as `data-test` |
| Auto-waiting | Actions wait until the element is ready |
| Persistent profile | Reuse a logged-in session between runs |
| Screenshots | Full-page evidence of what the script saw |

# Run the basic example
```powershell Setup and run
cd "Playwright Automation"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install playwright
python -m playwright install chromium
python Playwright_basic.py
```
The browser is headless, so no window appears. A successful run creates `google.png` in the current folder.

> [!TIP] Debugging
> Set `PWDEBUG=1` before a command to open the Playwright Inspector: `$env:PWDEBUG='1'; python script.py`. It lets you step through actions and test selectors live.

# Troubleshooting
| Problem | Fix |
| :-- | :-- |
| Chromium is missing | `python -m playwright install chromium` in the active environment |
| Browser download is blocked | Allow the terminal to download and run Playwright browsers |
| An element cannot be found | The site's HTML changed — inspect it and update the locator |

# Key takeaways
- Prefer stable attributes (`data-test`, roles, labels) over positions or fragile CSS paths.
- Let Playwright wait for elements instead of adding fixed sleeps.
- The two sub-projects have different dependencies and risks — follow each project's own README and explainer.
