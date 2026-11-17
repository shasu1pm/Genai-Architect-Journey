---
out: Phase-003-Robotic-Process-Automation-(RPA)/PyAutoGUI Automation/PyAutoGUI-Automation-Explainer.pdf
folder: Phase-003-Robotic-Process-Automation-(RPA)
title: PyAutoGUI Automation
subtitle: Desktop RPA — simulating a real mouse and keyboard to drive any Windows application
fact: Document | Sub-project explainer
fact: Level | Beginner
fact: Contents | 4 learning scripts · 2 complete bots
fact: Tools | Python · PyAutoGUI · Pyperclip · Pillow
fact: Folder | Phase-003-Robotic-Process-Automation-(RPA)/PyAutoGUI Automation
keywords: PyAutoGUI, desktop automation, RPA
---
# What it is
lead: PyAutoGUI moves the pointer, clicks, types and takes screenshots exactly as a person would.
Because it simulates physical input, PyAutoGUI can automate browsers and native Windows applications that offer no automation API. This folder teaches the basic operations, then applies them in two complete bots.

# What is in this folder
| File or project | Purpose |
| :-- | :-- |
| `basic_pyautogui.py` | Enables the upper-left-corner fail-safe and a one-second pause after actions |
| `pyautogui_mouse_operation.py` | Move, click, double-click, right-click and middle-click at `(100, 100)` |
| `pyautogui_keyboard_operation.py` | Types in the active window; select, copy, Enter and paste shortcuts |
| `pyautogui_screenshot_operation.py` | Captures the whole screen to `screenshot.png` |
| `Assignment-1-PyAutoGUI_Weather_Data/` | **Bengaluru Weather Bot** — AccuWeather to a dated Notepad file |
| `Assignment-2-PyAutoGUI_Bot_Stock_Price/` | **Apple Stock Price Bot** — Google Finance to a dated Excel report |

# The four building blocks
flow: Mouse > Keyboard > Clipboard > Screenshot
| Building block | Typical calls | Watch out for |
| :-- | :-- | :-- |
| Mouse | move, click, double-click, right-click | Coordinates are absolute screen pixels |
| Keyboard | typing text, `hotkey()` shortcuts | Keys go to whichever window has focus |
| Clipboard (Pyperclip) | read and write plain text | Copy only after the page has finished loading |
| Screenshot (needs Pillow) | full-screen capture | Re-running overwrites `screenshot.png` |

# Run the examples
```powershell Setup and run
cd "PyAutoGUI Automation"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pyautogui pyperclip pillow

python basic_pyautogui.py
python pyautogui_mouse_operation.py
python pyautogui_keyboard_operation.py
python pyautogui_screenshot_operation.py
```
Run one example at a time. Open Notepad before the keyboard example — the script gives you five seconds to focus it. Only run the mouse example when clicks near the top-left of the screen are harmless.

> [!NOTE] Safety first
> `pyautogui.FAILSAFE = True` stops a script when the pointer reaches the upper-left corner. The standalone mouse, keyboard and screenshot examples do not all set it, so keep `Ctrl+C` in the terminal ready.

# Important behaviour
- A different resolution, monitor layout or display scale changes where coordinates land.
- Timing matters: give windows and pages time to open before sending keys.
- The complete bots use `--check`-style preflights, waits and explicit messages so failures are readable.

# Key takeaways
- PyAutoGUI works with any application, at the cost of depending on focus, timing and layout.
- Combine it with Pyperclip to move text between applications through the clipboard.
- Always enable the fail-safe and keep the desktop untouched during a run.
- See the two bot explainers in the assignment folders for complete, specified automations.
