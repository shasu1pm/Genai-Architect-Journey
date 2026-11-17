---
out: Phase-003-Robotic-Process-Automation-(RPA)/Robotic-Process-Automation-Explainer.pdf
folder: Phase-003-Robotic-Process-Automation-(RPA)
title: Robotic Process Automation
subtitle: Teaching software to drive other software — the desktop with PyAutoGUI and the browser with Playwright
fact: Document | Phase explainer
fact: Level | Beginner to intermediate
fact: Tracks | PyAutoGUI (desktop) · Playwright (browser)
fact: Projects | Weather bot · Stock price bot · SauceDemo · WhatsApp bot
fact: Folder | Phase-003-Robotic-Process-Automation-(RPA)
keywords: RPA, PyAutoGUI, Playwright, automation
---
# What this phase is
lead: Robotic process automation (RPA) lets a script do the clicking, typing and copying a person would otherwise do by hand.
Phase-003-Robotic-Process-Automation-(RPA) demonstrates the two main approaches. **PyAutoGUI** drives the desktop by simulating a real mouse and keyboard. **Playwright** drives a browser through its own automation API. The phase moves from small learning scripts to complete bots that collect web data, write reports, send messages and save screenshots.

# Why it matters
- Many everyday business tasks are repetitive copy-and-paste work between applications.
- Automation is the first step towards AI agents: a program that perceives a screen or a page and acts on it.
- Knowing which tool fits a task — desktop or browser — avoids fragile solutions.

# The two tracks and six projects
| Track | Project | What it automates |
| :-- | :-- | :-- |
| PyAutoGUI | Fundamentals | Mouse, keyboard and screenshot operations |
| PyAutoGUI | Bengaluru Weather Bot | AccuWeather → parsed text → dated Notepad file |
| PyAutoGUI | Apple Stock Price Bot | Google Finance → Excel report → screenshot |
| Playwright | Fundamentals | Headless browser launch, navigation, screenshots |
| Playwright | SauceDemo Product Automation | Product extraction → screenshots → Excel report |
| Playwright | WhatsApp Automation Bot | Consent-based messaging, reply monitoring, reports |

# PyAutoGUI or Playwright — which one, and when
| PyAutoGUI | Playwright |
| :-- | :-- |
| Controls the physical mouse and keyboard | Controls the browser through its automation API |
| Automates desktop programs such as Excel and Notepad | Best for websites and browser applications |
| Depends on screen focus, timing, resolution and layout | Uses page elements and selectors — generally more reliable |
| Needs the desktop unlocked and untouched | Can run visibly or headless |
> [!TIP] A practical rule
> If the task lives entirely in a web page, use Playwright. If it must touch a desktop application with no API — Notepad, Excel — PyAutoGUI is the tool. The Apple Stock Price Bot shows both worlds meeting: a web page read through the browser, written into desktop Excel.

# How an automation is designed
flow: Specify each step > Pick the tool > Build with waits and checks > Save evidence > Handle failure safely
Every complete bot in this phase was written from a precise step-by-step specification first. Stating the steps and constraints before coding kept each script short and made its failure cases obvious.

# Run anything in this phase
```powershell General setup
cd "path\to\the\selected\project"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```
Then install the dependencies listed in that project's README and explainer PDF.

# Safety and responsible use
- PyAutoGUI scripts take over the active desktop — save other work and do not touch the mouse or keyboard. Moving the pointer to the upper-left corner triggers the fail-safe.
- Test with non-sensitive data first.
- Use the WhatsApp bot only with contacts who have explicitly agreed.
- Treat contact workbooks, browser profiles, reports and screenshots as private data.

# Key takeaways
- Desktop automation is flexible but fragile; browser automation is precise but browser-only.
- Specify first, then automate — waits, checks and evidence matter more than speed.
- Every folder in this phase has its own README, project document and explainer PDF.
- Next: Phase-004-FastAPI-And-Streamlit — turning scripts into products.
