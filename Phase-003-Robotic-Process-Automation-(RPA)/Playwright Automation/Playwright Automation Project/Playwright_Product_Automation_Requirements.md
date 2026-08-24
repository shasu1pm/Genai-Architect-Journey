# SauceDemo Automation — Requirements

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

## 1. Project Objective

Build a Python Playwright automation project that opens SauceDemo,
navigates through the product catalog, extracts product information,
saves the results to Excel, captures a screenshot for each product,
handles Windows 11 filename restrictions, records errors, and closes the
browser safely.

## 2. Target Website

**Website:** https://www.saucedemo.com/

## 3. Functional Requirements

### 3.1 Browser Launch

-   Open Google Chrome / Chromium using Playwright.
-   Run the browser in visible/headed mode for demonstration and
    testing.

### 3.2 Website Navigation

-   Navigate to the SauceDemo website.
-   Perform the required login and navigation actions.
-   Navigate to the product listing page.
-   Open each individual product page during processing.

### 3.3 Clicking and Form Filling

-   Identify required input fields using reliable Playwright locators.
-   Enter the required form values.
-   Click the appropriate buttons and links.
-   Handle navigation between the product listing page and individual
    product pages.

### 3.4 Waiting

-   Wait for the page and required dynamic elements to load before
    interacting with them.
-   Use Playwright's appropriate locator/waiting mechanisms rather than
    unnecessary fixed delays where possible.

### 3.5 Product Data Extraction

Extract the following information for every available product: - Product
Name - Product Price - Product URL - Current Date - Current Time

The Product URL must correspond to the individual product page.

## 4. Excel Reporting Requirements

Save all extracted product information into an Excel workbook.

### Required Excel Columns

  ----------------------------------------------------------------------------------
  Product    Price      Product    Date         Time       Screenshot     Status
  Name                  URL                                File           
  ---------- ---------- ---------- ------------ ---------- -------------- ----------
  Sauce Labs \$29.99    Product    08-08-2026   01:15:32   Sauce Labs     Success
  Backpack              URL                     PM         Backpack.png   

  Sauce Labs \$9.99     Product    08-08-2026   01:15:36   Sauce Labs     Success
  Bike Light            URL                     PM         Bike Light.png 
  ----------------------------------------------------------------------------------

### Excel Processing Rules

-   Create the Excel workbook automatically.
-   Add one row for each processed product.
-   Store the exact product URL.
-   Record the date and time when each product is processed.
-   Record the screenshot filename.
-   Include a **Status** column for success or failure information.
-   Save the Excel workbook after processing all products.

## 5. Screenshot Requirements

-   Take one screenshot for each individual product page.
-   The screenshot must correspond to the product currently being
    processed.
-   Save each screenshot as a `.png` file.
-   Use the Product Name as the screenshot filename.

Example:

``` text
Sauce Labs Backpack.png
Sauce Labs Bike Light.png
```

### 5.1 Product URL in Screenshot

Playwright's normal `page.screenshot()` captures the webpage content but
does not capture Chrome's outer browser interface/address bar.

Therefore, if the Product URL must be visibly included in the
screenshot, use one of these approaches:

1.  Display/inject the current Product URL as a visible header or
    overlay within the webpage before taking the screenshot; or
2.  Use an OS-level screenshot solution when capturing the actual
    browser address bar is a strict requirement.

For a Playwright-focused project, the preferred approach is to display
the current Product URL inside the webpage screenshot.

## 6. Windows 11 Screenshot Filename Handling

Because the Product Name is used as the `.png` filename, the automation
must sanitize filenames before saving them.

### Invalid Windows Filename Characters

The following characters must be removed or safely replaced:

``` text
< > : " / \ | ? *
```

### Filename Rules

-   Replace/remove invalid Windows filename characters.
-   Remove trailing spaces.
-   Remove trailing periods.
-   Prevent empty filenames.
-   Handle Windows reserved filenames.
-   Limit excessively long filenames.
-   Preserve the `.png` extension.

Example:

``` text
Original Product Name:
Backpack: Blue / Large?

Safe Screenshot Filename:
Backpack_ Blue _ Large_.png
```

## 7. Duplicate Filename Handling

If multiple products result in the same sanitized filename, do not
overwrite an existing screenshot.

Example:

``` text
Sauce Labs Backpack.png
Sauce Labs Backpack_2.png
Sauce Labs Backpack_3.png
```

## 8. Screenshot Directory

-   Create a dedicated screenshot directory automatically.
-   Check whether the directory exists before saving.
-   Create it when it does not exist.

Example project structure:

``` text
project/
├── main.py
├── products.xlsx
└── screenshots/
    ├── Sauce Labs Backpack.png
    ├── Sauce Labs Bike Light.png
    └── ...
```

## 9. Error Handling

The automation must include exception handling.

Requirements: - Failure while processing one product must not terminate
the complete automation. - Catch and record product-level errors. -
Continue processing the remaining products whenever possible. - Record
failure details in the Excel **Status** column. - Handle screenshot save
failures. - Handle navigation failures. - Handle missing product
elements. - Handle Excel save errors appropriately.

Example status values:

``` text
Success
Failed - Product price not found
Failed - Screenshot could not be saved
Failed - Product page navigation error
```

## 10. Browser Cleanup

-   Close the browser safely after processing is complete.
-   Ensure browser cleanup occurs even if an exception is raised.
-   Use appropriate `try`, `except`, and `finally` handling where
    required.

## 11. End-to-End Automation Flow

``` text
START
  ↓
Launch Chrome / Chromium
  ↓
Open SauceDemo
  ↓
Fill Login Form
  ↓
Click Login
  ↓
Wait for Product Listing
  ↓
Collect Products
  ↓
Open Individual Product
  ↓
Extract Product Name
  ↓
Extract Price
  ↓
Capture Product URL
  ↓
Capture Current Date + Time
  ↓
Sanitize Product Name for Windows Filename
  ↓
Handle Duplicate Filename
  ↓
Take Product Screenshot
  ↓
Record Data + Screenshot Filename + Status
  ↓
Continue to Next Product
  ↓
Save All Results to Excel
  ↓
Close Browser Safely
  ↓
END
```

## 12. Expected Deliverables

The completed project should produce:

-   A working Python Playwright automation script.
-   An Excel report containing all extracted product records.
-   A screenshot for every successfully processed product.
-   Windows 11-safe screenshot filenames based on product names.
-   Product URLs and processing timestamps.
-   Success/error status information for every processed product.
-   Reliable exception handling and browser cleanup.

## 13. Suggested Technology Stack

-   Python
-   Playwright for Python
-   Chromium / Google Chrome
-   openpyxl for Excel workbook creation
-   Python `datetime` for date and time
-   Python `pathlib` / `os` for file and directory handling
-   Python `re` for filename sanitization

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank" rel="noopener">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank" rel="noopener">LinkedIn</a>
