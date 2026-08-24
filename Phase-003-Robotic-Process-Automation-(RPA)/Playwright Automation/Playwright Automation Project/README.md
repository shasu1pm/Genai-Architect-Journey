# SauceDemo Product Automation

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

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
