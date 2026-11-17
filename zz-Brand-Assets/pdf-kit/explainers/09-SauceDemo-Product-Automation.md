---
out: Phase-003-Robotic-Process-Automation-(RPA)/Playwright Automation/Playwright Automation Project/SauceDemo-Product-Automation-Explainer.pdf
folder: Phase-003-Robotic-Process-Automation-(RPA)
title: SauceDemo Product Automation
subtitle: Sign in to a demo store, visit every product, capture screenshots and write a formatted Excel report
fact: Document | Sub-project explainer
fact: Level | Intermediate
fact: Script | Playwright_Web_Automation.py
fact: Tools | Python · Playwright (Chromium) · openpyxl
fact: Output | products.xlsx + screenshots/ (one per product)
fact: Folder | …/Playwright Automation/Playwright Automation Project
keywords: Playwright, SauceDemo, Excel, screenshots, web scraping
---
# What it does
lead: A complete browser-automation project against SauceDemo, a public practice store built for testing.
The script signs in, opens each product page, extracts the product information, takes one screenshot per product and writes everything to a formatted Excel workbook.

# The workflow
flow: Sign in > List products > Open each product > Extract details > Screenshot with URL overlay > Write Excel report
| Collected field | Notes |
| :-- | :-- |
| Product name and price | Read through SauceDemo's stable `data-test` attributes |
| Detail-page URL | Also drawn onto the screenshot, because browser screenshots omit the address bar |
| Date and time | When the product was captured |
| Screenshot filename | Windows-safe and unique — a numeric suffix avoids overwriting |
| Status | Per-product success or the error encountered |

# Run it
```powershell Setup and run
cd "Playwright Automation\Playwright Automation Project"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install playwright openpyxl
python -m playwright install chromium

python Playwright_Web_Automation.py
python Playwright_Web_Automation.py --output "output\products.xlsx" --screenshots "output\screenshots"
```
The parser also offers `--headless`, but the current code launches with `headless=False`, so the browser stays visible until that setting is changed in the source.

> [!NOTE] Public demo credentials
> SauceDemo publishes its training login: `standard_user` / `secret_sauce`. They are built into the script and can be overridden with `SAUCEDEMO_USERNAME` and `SAUCEDEMO_PASSWORD`. Real credentials always belong in environment variables, never in code.

# What makes it robust
- **Partial results survive:** one product's error is recorded in `Status` instead of losing the whole report.
- **Readable workbook:** formatted header, frozen top row, filter, sized columns and clickable URLs.
- **Clear exit codes:** `0` when the run completes, `1` for a top-level automation or save error.

# Troubleshooting
| Problem | Fix |
| :-- | :-- |
| Login fails | Check internet access and that SauceDemo is available |
| Chromium missing | `python -m playwright install chromium` |
| Locators fail | SauceDemo may have changed its `data-test` values or routes |
| Workbook will not save | Close `products.xlsx` in Excel or choose another `--output` |

# Key takeaways
- `data-test` attributes are the most stable selectors a site can offer.
- Record per-item status so one failure never destroys the whole run.
- Evidence matters: the URL overlay makes every screenshot self-explaining.
