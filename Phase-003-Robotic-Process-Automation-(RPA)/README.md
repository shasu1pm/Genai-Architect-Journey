# RPA — Robotic Process Automation

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

**Teaching software to drive other software — the desktop and the browser.**

A collection of Python projects that demonstrate two approaches to robotic process automation (RPA): desktop automation with **PyAutoGUI** and browser automation with **Playwright**. The phase includes small learning examples as well as complete bots that collect web data, create reports, send messages, and save screenshots.

---

## Quick Navigation

| # | Track | What it covers | Go to |
| :-- | :-- | :-- | :-- |
| 1 | **PyAutoGUI** | Driving the desktop by simulating a real mouse and keyboard | [Open](./PyAutoGUI%20Automation/) |
| 2 | **Playwright** | Driving the browser through its own automation API | [Open](./Playwright%20Automation/) |

📄 **Phase document:** [RPA - Robotic Process Automation.pdf](./RPA%20-%20Robotic%20Process%20Automation.pdf)

---

## Documents

Every folder in this phase carries its own README and a matching branded PDF.

| Folder | Document |
| :-- | :-- |
| *This phase* | [RPA - Robotic Process Automation.pdf](./RPA%20-%20Robotic%20Process%20Automation.pdf) |
| [PyAutoGUI Automation](./PyAutoGUI%20Automation/) | [PyAutoGUI Automation.pdf](./PyAutoGUI%20Automation/PyAutoGUI%20Automation.pdf) |
| [↳ Bengaluru Weather Bot](./PyAutoGUI%20Automation/Assignment-1-PyAutoGUI_Weather_Data/) | [Bengaluru Weather Bot.pdf](./PyAutoGUI%20Automation/Assignment-1-PyAutoGUI_Weather_Data/Bengaluru%20Weather%20Bot.pdf) |
| [↳ Apple Stock Price Bot](./PyAutoGUI%20Automation/Assignment-2-PyAutoGUI_Bot_Stock_Price/) | [Apple Stock Price Bot.pdf](./PyAutoGUI%20Automation/Assignment-2-PyAutoGUI_Bot_Stock_Price/Apple%20Stock%20Price%20Bot.pdf) |
| [Playwright Automation](./Playwright%20Automation/) | [Playwright Automation.pdf](./Playwright%20Automation/Playwright%20Automation.pdf) |
| [↳ SauceDemo Product Automation](./Playwright%20Automation/Playwright%20Automation%20Project/) | [SauceDemo Product Automation.pdf](./Playwright%20Automation/Playwright%20Automation%20Project/SauceDemo%20Product%20Automation.pdf) |
| [↳ WhatsApp Automation Bot](./Playwright%20Automation/Playwright%20Assignment/) | [WhatsApp Automation Bot.pdf](./Playwright%20Automation/Playwright%20Assignment/WhatsApp%20Automation%20Bot.pdf) |

---

## Project overview

| Track | Project | What it automates |
| --- | --- | --- |
| PyAutoGUI | [Fundamentals](./PyAutoGUI%20Automation/) | Mouse, keyboard, and screenshot operations |
| PyAutoGUI | [Bengaluru Weather Bot](./PyAutoGUI%20Automation/Assignment-1-PyAutoGUI_Weather_Data/) | AccuWeather → parsed text → Notepad file |
| PyAutoGUI | [Apple Stock Price Bot](./PyAutoGUI%20Automation/Assignment-2-PyAutoGUI_Bot_Stock_Price/) | Google Finance → Excel report → screenshot |
| Playwright | [Fundamentals](./Playwright%20Automation/) | Headless browser launch, navigation, and screenshots |
| Playwright | [SauceDemo Product Automation](./Playwright%20Automation/Playwright%20Automation%20Project/) | Product extraction → screenshots → Excel report |
| Playwright | [WhatsApp Automation Bot](./Playwright%20Automation/Playwright%20Assignment/) | Consent-based messaging, reply monitoring, and reports |

## PyAutoGUI versus Playwright

| PyAutoGUI | Playwright |
| --- | --- |
| Controls the physical mouse and keyboard | Controls the browser through its automation API |
| Can automate desktop programs such as Excel and Notepad | Best suited to websites and browser applications |
| Depends on screen focus, timing, resolution, and UI position | Uses page elements and selectors, so it is generally more reliable |
| Requires the desktop to remain unlocked and untouched | Can run visibly or headlessly, depending on the script |

## Repository structure

```text
Phase-003-Robotic-Process-Automation-(RPA)/
├── README.md
├── .gitignore
├── RPA - Robotic Process Automation.pdf
│
├── PyAutoGUI Automation/
│   ├── README.md
│   ├── PyAutoGUI Automation.pdf
│   ├── basic_pyautogui.py                     # Fail-safe and pause settings
│   ├── pyautogui_mouse_operation.py           # Move, click, double, right, middle
│   ├── pyautogui_keyboard_operation.py        # Typing and shortcut keys
│   ├── pyautogui_screenshot_operation.py      # Full-screen capture
│   ├── screenshot.png                         # Sample capture
│   ├── Assignment-1-PyAutoGUI_Weather_Data/
│   │   ├── README.md
│   │   ├── Bengaluru Weather Bot.pdf
│   │   ├── Assignment1_Weather_Data.py
│   │   └── YYYY-MM-DD_Weather_Data.txt        # Sample runs
│   └── Assignment-2-PyAutoGUI_Bot_Stock_Price/
│       ├── README.md
│       ├── Apple Stock Price Bot.pdf
│       ├── requirements.txt
│       ├── daily_report_bot.py
│       └── output/                            # Dated Excel reports + screenshots
│
└── Playwright Automation/
    ├── README.md
    ├── Playwright Automation.pdf
    ├── Playwright_basic.py                    # Headless launch and screenshot
    ├── Playwright_Functionality.py            # Capability reference
    ├── Playwright Automation Project/
    │   ├── README.md
    │   ├── SauceDemo Product Automation.pdf
    │   ├── Playwright_Product_Automation_Requirements.md
    │   ├── Playwright_Web_Automation.py
    │   ├── products.xlsx                      # Generated report
    │   └── screenshots/                       # One per product
    └── Playwright Assignment/
        ├── README.md
        ├── WhatsApp Automation Bot.pdf
        ├── Playwright-WhatsApp Automation Bot.md
        ├── Playwright-WhatsApp-Automation-Bot.py
        ├── .gitignore
        └── Error Fix 1.png, Error Fix 2.png   # Development notes
```

> [!NOTE]
> Generated reports, screenshots, local browser profiles, and virtual environments are supporting artifacts of a run, not separate projects.
>
> **Not committed:** screen recordings (80–100 MB each), `contacts.xlsx`, the WhatsApp browser profile, and generated conversation reports. The `.gitignore` in this folder excludes them — recordings are large enough to be rejected by GitHub, and the rest can contain personal data.

## Requirements

- Windows 10 or Windows 11 for the desktop-automation assignments
- Python 3.10 or newer
- Internet access
- Google Chrome for the PyAutoGUI web-data bots
- Microsoft Excel for the stock-price bot
- Microsoft Edge and a WhatsApp account for the WhatsApp bot

Each project has its own setup and run instructions in its local README. Create a fresh virtual environment inside the project you want to run — virtual environments are machine-specific and are never committed.

## General setup

```powershell
cd "path\to\the\selected\project"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Then install the dependencies shown in that project's README.

## Safety and responsible use

- PyAutoGUI scripts take control of the active desktop. Save other work, keep the desktop unlocked, and do not use the mouse or keyboard during a run.
- PyAutoGUI's fail-safe is enabled in the complete desktop bots. Move the pointer to the upper-left corner to stop the automation.
- Test automation with non-sensitive data before using real accounts or documents.
- Use the WhatsApp bot only with contacts who have explicitly consented. Automated messaging may be subject to WhatsApp's terms and account restrictions.
- Treat `contacts.xlsx`, WhatsApp browser profiles, conversation reports, and screenshots as private data. Do not publish them without review and redaction.

## Known limitations

Websites and desktop interfaces change over time. Page selectors, copied page text, application shortcuts, or screen coordinates may eventually need adjustment. Display scaling, pop-ups, cookie dialogs, slow connections, and window focus can also affect desktop automation.

## License

No license file is currently included. Unless the owner adds one, the source code should be treated as all rights reserved.

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank" rel="noopener">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank" rel="noopener">LinkedIn</a>
