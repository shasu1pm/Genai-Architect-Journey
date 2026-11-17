<!-- brand:header:start -->
<p align="center">
  <img src="../../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# Apple Stock Price Bot

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

📘 **Explainer:** [Apple-Stock-Price-Bot-Explainer.pdf](./Apple-Stock-Price-Bot-Explainer.pdf) — this folder in a short, branded guide.


This project implements only the **stock-price** option from the assignment.
It uses PyAutoGUI to:

📄 **Project document:** [Apple Stock Price Bot.pdf](./Apple%20Stock%20Price%20Bot.pdf)

1. Open the Apple (`AAPL`) quote on Google Finance in Chrome.
2. Copy the visible webpage text and extract the current stock price.
3. Open Microsoft Excel and create a row containing:
   - Date & Time
   - Stock Company Name
   - Stock Data
   - Source link
   - Comment
4. Save a dated workbook such as `daily_report_2026-07-28.xlsx`.
5. Save a screenshot of the final Excel sheet.

All automation code is in the required single file, `daily_report_bot.py`. The bot is configured for Apple Inc. (`AAPL`) on NASDAQ and reads the quote from Google Finance.

## Requirements

- Windows 10 or Windows 11
- Python 3.10+
- Google Chrome
- Microsoft Excel desktop edition
- Internet access

## Windows setup

Open PowerShell in this project folder. Create a fresh local environment instead of relying on the bundled machine-specific `venv` directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run a safe preflight check:

```powershell
python daily_report_bot.py --check
```

Run the automation:

```powershell
python daily_report_bot.py
```

Do not touch the keyboard or mouse while the bot runs. Move the pointer to the
top-left corner of the screen to trigger PyAutoGUI's emergency stop.

Generated `.xlsx` and `.png` files are placed in the `output` folder. If a
report for the current date already exists, the bot adds the current time to
the new filenames instead of overwriting the earlier report.

```text
output/
├── daily_report_YYYY-MM-DD.xlsx
└── daily_report_YYYY-MM-DD_screenshot.png
```

The workbook contains `Date & Time`, `Stock Company Name`, `Stock Data`, `Source link`, and `Comment` columns. The code formats the header and auto-fits the populated columns through Excel keyboard shortcuts.

## How it works

1. Locates Chrome and Excel in their standard Windows installation paths.
2. Opens the Apple quote in a new Chrome window and copies the visible page text.
3. Finds a USD price near the `Apple Inc` heading.
4. Opens a blank Excel workbook and pastes a tab-separated header and data row.
5. saves the workbook and captures the visible Excel sheet.

`python daily_report_bot.py --check` performs only the application and output-directory checks; it does not open the website or control the desktop.

## Notes

- Google Chrome and Microsoft Excel must be installed in their standard
  Windows locations.
- Internet access is required.
- If the page loads slowly, increase `PAGE_LOAD_SECONDS` near the top of
  `daily_report_bot.py`.
- Close any Chrome consent dialog before retrying if the bot reports that the
  Google Finance data was not copied.
- The bot first sends `Ctrl+N` after Excel starts. On Excel versions where that
  shortcut opens the **New** template page, it automatically selects the
  **Blank workbook** tile before entering data.
- The bot is intentionally specific to Apple. Change `STOCK_SYMBOL`, `EXCHANGE`, `COMPANY_NAME`, and the extraction assumptions together if adapting it to another security.
- Google Finance content and Excel UI behavior can change. If the page labels or application layout changes, the selectors, parsing, or UI actions may need adjustment.

## Safety

Save other work and avoid using the desktop during a run. PyAutoGUI's fail-safe is enabled: move the pointer to the upper-left corner to stop the bot. Stock quotes may be delayed and this educational project is not financial advice or a trading system.

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
  <a href="https://shasuvathanan.com"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/website-personal-logo.png" alt="Website" title="Website" height="24"></a>
  &nbsp;
  <a href="mailto:shasu1pm@gmail.com"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/Gmail_Logo.svg" alt="Email" title="Email" height="24"></a>
  &nbsp;
  <a href="https://linkedin.com/in/shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/linkedin.png" alt="LinkedIn" title="LinkedIn" height="24"></a>
  &nbsp;
  <a href="https://github.com/shasu1pm"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/github-custom.png" alt="GitHub" title="GitHub" height="24"></a>
  &nbsp;
  <a href="https://huggingface.co/Shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/huggingface.png" alt="Hugging Face" title="Hugging Face" height="24"></a>
  &nbsp;
  <a href="https://www.youtube.com/@ShasuVathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/youtube.png" alt="YouTube" title="YouTube" height="24"></a>
  &nbsp;
  <a href="https://x.com/shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/x.png" alt="X (Twitter)" title="X (Twitter)" height="24"></a>
  &nbsp;
  <a href="https://higgsfield.ai/@shasuvathanan"><img src="../../../zz-Brand-Assets/Social-Media-Logos/PNG/Higgsfield_AI.png" alt="Higgsfield AI" title="Higgsfield AI" height="24"></a>
  <br>
  <sub><b>Connect:</b> <a href="https://shasuvathanan.com">Website</a> &nbsp;&#8226;&nbsp; <a href="mailto:shasu1pm@gmail.com">Email</a> &nbsp;&#8226;&nbsp; <a href="https://linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm">GitHub</a> &nbsp;&#8226;&nbsp; <a href="https://huggingface.co/Shasuvathanan">Hugging Face</a> &nbsp;&#8226;&nbsp; <a href="https://www.youtube.com/@ShasuVathanan">YouTube</a> &nbsp;&#8226;&nbsp; <a href="https://x.com/shasuvathanan">X (Twitter)</a> &nbsp;&#8226;&nbsp; <a href="https://higgsfield.ai/@shasuvathanan">Higgsfield AI</a></sub>
</p>
<!-- brand:social:end -->
<p align="center">
  <img src="../../../zz-Brand-Assets/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>Shasu Vathanan - GEN AI - Product Manager</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; <a href="../../../README.md">Back to the journey index</a></sub>
</p>
<!-- brand:footer:end -->
