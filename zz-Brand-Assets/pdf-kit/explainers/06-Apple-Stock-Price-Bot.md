---
out: Phase-003-Robotic-Process-Automation-(RPA)/PyAutoGUI Automation/Assignment-2-PyAutoGUI_Bot_Stock_Price/Apple-Stock-Price-Bot-Explainer.pdf
folder: Phase-003-Robotic-Process-Automation-(RPA)
title: Apple Stock Price Bot
subtitle: Read Apple's (AAPL) price from Google Finance and build a dated Excel report with a screenshot
fact: Document | Sub-project explainer
fact: Level | Intermediate
fact: Script | daily_report_bot.py (single file)
fact: Tools | Python · PyAutoGUI · Chrome · Microsoft Excel
fact: Output | output/daily_report_YYYY-MM-DD.xlsx + screenshot
fact: Folder | …/PyAutoGUI Automation/Assignment-2-PyAutoGUI_Bot_Stock_Price
keywords: PyAutoGUI, Excel, stock price, Apple, Google Finance
---
# What it does
lead: A daily report bot: one company, one price, one dated Excel row, and a screenshot as proof.
The bot opens the Apple Inc. (`AAPL`, NASDAQ) quote on Google Finance in Chrome, copies the visible page text, extracts the current price, then opens Microsoft Excel and writes a report row before saving the workbook and a screenshot of the sheet.

# Why Apple is the example
Apple is a familiar, heavily traded company, so its quote page is always available and easy to check by eye. The bot is deliberately specific to it: adapting to another company means changing `STOCK_SYMBOL`, `EXCHANGE`, `COMPANY_NAME` and the extraction assumptions together.

# The workflow
flow: Locate Chrome + Excel > Open AAPL quote > Copy page text > Find USD price > Paste row into Excel > Save workbook + screenshot
| Column | Contents |
| :-- | :-- |
| Date & Time | When the price was captured |
| Stock Company Name | Apple Inc. |
| Stock Data | The extracted USD price |
| Source link | The Google Finance URL |
| Comment | A short note about the capture |

# Run it
```powershell Setup, preflight and run
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

python daily_report_bot.py --check     # safe preflight: checks apps and output folder only
python daily_report_bot.py             # full run — do not touch mouse or keyboard
```
```text Output
output/
├── daily_report_YYYY-MM-DD.xlsx
└── daily_report_YYYY-MM-DD_screenshot.png
```
If a report for today already exists, the time is added to the new filenames instead of overwriting the earlier report.

> [!TIP] Good automation habits shown here
> A `--check` preflight that never touches the desktop; a fail-safe corner; tab-separated paste so Excel splits columns by itself; keyboard shortcuts to format the header and auto-fit columns; and a fallback that picks the **Blank workbook** tile when `Ctrl+N` opens Excel's template page instead.

# Notes and limits
- Chrome and Excel must be in their standard Windows locations; internet access is required.
- If the page loads slowly, increase `PAGE_LOAD_SECONDS` near the top of the script.
- Google Finance content and Excel's interface can change; parsing or UI steps may then need updating.
- Quotes may be delayed. This is an educational project — not financial advice or a trading system.

# Key takeaways
- Desktop RPA shines when the destination is a desktop application such as Excel.
- Avoid overwriting evidence: date and time in filenames keep every run.
- A preflight check catches missing applications before the bot takes over the screen.
