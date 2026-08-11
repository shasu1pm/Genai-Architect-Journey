# RPA — Robotic Process Automation

A collection of Python projects that demonstrate two approaches to robotic process automation (RPA): desktop automation with **PyAutoGUI** and browser automation with **Playwright**. The repository includes small learning examples as well as complete bots that collect web data, create reports, send messages, and save screenshots.

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
RPA-Robotic Process Automation/
├── README.md
├── PyAutoGUI Automation/
│   ├── README.md
│   ├── basic_pyautogui.py
│   ├── pyautogui_mouse_operation.py
│   ├── pyautogui_keyboard_operation.py
│   ├── pyautogui_screenshot_operation.py
│   ├── Assignment-1-PyAutoGUI_Weather_Data/
│   │   ├── README.md
│   │   └── Assignment1_Weather_Data.py
│   └── Assignment-2-PyAutoGUI_Bot_Stock_Price/
│       ├── README.md
│       ├── requirements.txt
│       └── daily_report_bot.py
└── Playwright Automation/
    ├── README.md
    ├── Playwright_basic.py
    ├── Playwright_Functionality.py
    ├── Playwright Automation Project/
    │   ├── README.md
    │   └── Playwright_Web_Automation.py
    └── Playwright Assignment/
        ├── README.md
        └── Playwright-WhatsApp-Automation-Bot.py
```

Generated reports, screenshots, recordings, local browser profiles, and virtual environments are supporting artifacts and are not separate projects.

## Requirements

- Windows 10 or Windows 11 for the desktop-automation assignments
- Python 3.10 or newer
- Internet access
- Google Chrome for the PyAutoGUI web-data bots
- Microsoft Excel for the stock-price bot
- Microsoft Edge and a WhatsApp account for the WhatsApp bot

Each project has its own setup and run instructions in its local README. Create a separate virtual environment inside the project you want to run; do not rely on the checked-in `venv` directories because virtual environments are machine-specific.

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

**Contributing**

Feel free to fork this repository, improve the content, and share your knowledge with the community.

**Created and Maintained by:**

**Shasu Vathanan**  **•**  **Gen AI Product Manager**
