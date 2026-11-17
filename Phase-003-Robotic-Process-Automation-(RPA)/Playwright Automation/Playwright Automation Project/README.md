<!-- brand:header:start -->
<p align="center">
  <img src="../../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# SauceDemo Product Automation

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

📘 **Explainer:** [SauceDemo-Product-Automation-Explainer.pdf](./SauceDemo-Product-Automation-Explainer.pdf) — this folder in a short, branded guide.


A Python and Playwright project that signs in to the SauceDemo training store, visits each product page, extracts product information, captures one screenshot per product, and writes a formatted Excel report.

📄 **Project document:** [SauceDemo Product Automation.pdf](./SauceDemo%20Product%20Automation.pdf)

## Features

- Uses SauceDemo's stable `data-test` attributes for element selection.
- Collects product name, price, detail-page URL, date, time, screenshot filename, and status.
- Adds the product URL as a visible overlay before each screenshot because browser screenshots do not include the address bar.
- Creates Windows-safe, unique screenshot filenames.
- Saves partial results and per-product errors instead of losing the entire report after one failure.
- Formats the Excel header, freezes it, adds a filter, sizes columns, and makes URLs clickable.

## Requirements

- Python 3.10+
- Internet access
- Playwright with Chromium
- `openpyxl`

## Setup

```powershell
cd "Playwright Automation\Playwright Automation Project"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install playwright openpyxl
python -m playwright install chromium
```

## Run

```powershell
python Playwright_Web_Automation.py
```

The script accepts these command-line options:

```powershell
python Playwright_Web_Automation.py --output "output\products.xlsx" --screenshots "output\screenshots"
python Playwright_Web_Automation.py --help
```

`--output` changes the workbook path, and `--screenshots` changes the screenshot directory. The parser also exposes `--headless`; however, the current implementation explicitly launches with `headless=False`, so the browser remains visible until that launch setting is changed in the source.

## Credentials

The default SauceDemo training credentials are built into the script:

```text
Username: standard_user
Password: secret_sauce
```

They can be overridden for the current PowerShell session:

```powershell
$env:SAUCEDEMO_USERNAME = "standard_user"
$env:SAUCEDEMO_PASSWORD = "secret_sauce"
python Playwright_Web_Automation.py
```

## Output

By default, the project writes:

```text
products.xlsx
screenshots/
├── Sauce Labs Backpack.png
├── Sauce Labs Bike Light.png
└── ...
```

If a screenshot filename already exists, a numeric suffix is added rather than overwriting it. The workbook itself is overwritten when the same output path is reused.

The included `products.xlsx` and `screenshots/` are example results. `Playwright_Product_Automation_Requirements.md` and the Word document preserve the original assignment specification.

## Exit behavior and troubleshooting

The command exits with code `0` when the overall automation completes, or `1` when a top-level automation or workbook-save error occurs. Individual product problems are recorded in the `Status` column.

- If login fails, verify internet access and SauceDemo availability.
- If Chromium is missing, run `python -m playwright install chromium`.
- If product locators fail, SauceDemo may have changed its `data-test` values or routes.
- If `products.xlsx` is open in Excel, close it or select a different `--output` path before rerunning.

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
