<!-- brand:header:start -->
<p align="center">
  <img src="../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# PyAutoGUI Automation

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

📘 **Explainer:** [PyAutoGUI-Automation-Explainer.pdf](./PyAutoGUI-Automation-Explainer.pdf) — this folder in a short, branded guide.


This folder introduces desktop RPA with PyAutoGUI and contains two complete assignments. PyAutoGUI simulates physical mouse and keyboard actions, so it can work with browsers and native Windows applications that do not expose an automation API.

📄 **Project document:** [PyAutoGUI Automation.pdf](./PyAutoGUI%20Automation.pdf)

## Contents

| File or project | Purpose |
| --- | --- |
| `basic_pyautogui.py` | Imports PyAutoGUI, enables the upper-left-corner fail-safe, and adds a one-second pause after actions |
| `pyautogui_mouse_operation.py` | Demonstrates move, click, double-click, right-click, and middle-click operations at `(100, 100)` |
| `pyautogui_keyboard_operation.py` | Types in the active application and demonstrates select, copy, Enter, and paste shortcuts |
| `pyautogui_screenshot_operation.py` | Captures the complete screen to `screenshot.png` |
| [Assignment 1 — Weather Data](./Assignment-1-PyAutoGUI_Weather_Data/) | Captures current Bengaluru weather and saves a dated Notepad document |
| [Assignment 2 — Stock Price](./Assignment-2-PyAutoGUI_Bot_Stock_Price/) | Captures Apple's stock price and builds a dated Excel report |

## Setup

```powershell
cd "PyAutoGUI Automation"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pyautogui pyperclip pillow
```

`Pillow` is required by PyAutoGUI's screenshot feature.

## Run the examples

```powershell
python basic_pyautogui.py
python pyautogui_mouse_operation.py
python pyautogui_keyboard_operation.py
python pyautogui_screenshot_operation.py
```

Run one example at a time. Before running the keyboard example, open Notepad or another safe text editor; the script gives you five seconds to focus it. The mouse example immediately operates near the upper-left portion of the screen, so use it only when clicks at those coordinates are harmless.

## Important behavior

- Coordinates are absolute screen pixels and can behave differently with another resolution, monitor layout, or display scale.
- Keyboard input is sent to whichever window has focus.
- `pyautogui_screenshot_operation.py` overwrites `screenshot.png` when it is run again from this directory.
- The standalone mouse, keyboard, and screenshot examples do not all configure `FAILSAFE`; use `Ctrl+C` from the terminal if needed.

For full setup, outputs, and troubleshooting, open the README inside the relevant assignment directory.

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
  <a href="https://shasuvathanan.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/website-personal-logo.png" alt="Website" title="Website" height="24"></a>
  &nbsp;
  <a href="mailto:shasu1pm@gmail.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Gmail_Logo.svg" alt="Email" title="Email" height="24"></a>
  &nbsp;
  <a href="https://linkedin.com/in/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/linkedin.png" alt="LinkedIn" title="LinkedIn" height="24"></a>
  &nbsp;
  <a href="https://github.com/shasu1pm"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/github-custom.png" alt="GitHub" title="GitHub" height="24"></a>
  &nbsp;
  <a href="https://huggingface.co/Shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/huggingface.png" alt="Hugging Face" title="Hugging Face" height="24"></a>
  &nbsp;
  <a href="https://www.youtube.com/@ShasuVathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/youtube.png" alt="YouTube" title="YouTube" height="24"></a>
  &nbsp;
  <a href="https://x.com/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/x.png" alt="X (Twitter)" title="X (Twitter)" height="24"></a>
  &nbsp;
  <a href="https://higgsfield.ai/@shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Higgsfield_AI.png" alt="Higgsfield AI" title="Higgsfield AI" height="24"></a>
  <br>
  <sub><b>Connect:</b> <a href="https://shasuvathanan.com">Website</a> &nbsp;&#8226;&nbsp; <a href="mailto:shasu1pm@gmail.com">Email</a> &nbsp;&#8226;&nbsp; <a href="https://linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm">GitHub</a> &nbsp;&#8226;&nbsp; <a href="https://huggingface.co/Shasuvathanan">Hugging Face</a> &nbsp;&#8226;&nbsp; <a href="https://www.youtube.com/@ShasuVathanan">YouTube</a> &nbsp;&#8226;&nbsp; <a href="https://x.com/shasuvathanan">X (Twitter)</a> &nbsp;&#8226;&nbsp; <a href="https://higgsfield.ai/@shasuvathanan">Higgsfield AI</a></sub>
</p>
<!-- brand:social:end -->
<p align="center">
  <img src="../../zz-Brand-Assets/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>Shasu Vathanan - GEN AI - Product Manager</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; <a href="../../README.md">Back to the journey index</a></sub>
</p>
<!-- brand:footer:end -->
