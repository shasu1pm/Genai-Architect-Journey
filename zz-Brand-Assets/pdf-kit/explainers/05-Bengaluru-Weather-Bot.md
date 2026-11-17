---
out: Phase-003-Robotic-Process-Automation-(RPA)/PyAutoGUI Automation/Assignment-1-PyAutoGUI_Weather_Data/Bengaluru-Weather-Bot-Explainer.pdf
folder: Phase-003-Robotic-Process-Automation-(RPA)
title: Bengaluru Weather Bot
subtitle: A desktop bot that reads current weather from AccuWeather and saves a dated Notepad report
fact: Document | Sub-project explainer
fact: Level | Beginner to intermediate
fact: Script | Assignment1_Weather_Data.py
fact: Tools | Python · PyAutoGUI · Pyperclip · Chrome · Notepad
fact: Output | YYYY-MM-DD_Weather_Data.txt
fact: Folder | …/PyAutoGUI Automation/Assignment-1-PyAutoGUI_Weather_Data
keywords: PyAutoGUI, weather, Notepad, regular expressions
---
# What it does
lead: Open AccuWeather, copy the page, find the current readings, and save them as a dated text file — without touching the mouse.
The bot opens AccuWeather's Bengaluru current-weather page in Google Chrome, copies the visible page text, extracts the current weather values, pastes a formatted report into Notepad and saves it with a date-based filename.

# The workflow
flow: Launch Chrome > Open AccuWeather > Copy page text > Parse current weather > Paste into Notepad > Save dated file
| Step | Requirement |
| :-- | :-- |
| 1 | Open the Chrome browser |
| 2 | Open the AccuWeather Bengaluru current-weather page in a new tab |
| 3 | Copy the **values** inside the Current Weather section — not just the heading |
| 4 | Open Notepad and start a new document |
| 5 | Paste the parsed weather data |
| 6 | Save as `{Today Date}_Weather_Data.txt` |

# What the report contains
Temperature, RealFeel, condition, wind, gusts, humidity, indoor humidity, dew point, pressure, cloud cover, visibility, cloud ceiling, capture time and the source URL. Any value the parser cannot identify is written as `Not found` instead of stopping the run.

# The hard part — step 3
Copying the page is easy; deciding which copied lines are the current readings is the real work. That is why the parser uses **labelled regular expressions** (find "Humidity", then the value beside it) rather than fixed line positions, which would break the moment the page layout shifts.

# Run it
```powershell Setup and run
cd "PyAutoGUI Automation\Assignment-1-PyAutoGUI_Weather_Data"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pyautogui pyperclip pillow
python Assignment1_Weather_Data.py
```
> [!NOTE] Three constraints shaped the design
> Chrome must stay visible and focused while copying, because PyAutoGUI sends shortcuts to the focused window. The desktop must be left alone — the upper-left corner triggers the emergency stop. `hotkey()` sends Ctrl+C / Ctrl+V while Pyperclip reads the clipboard text.

# Configuration
| Setting | Meaning |
| :-- | :-- |
| `WEATHER_URL` | Which AccuWeather location and page to open |
| `PROJECT_FOLDER = os.getcwd()` | Output goes to the folder Python is launched from |
| 15-second page-load wait | Increase it for slower connections |

# Troubleshooting
| Symptom | Fix |
| :-- | :-- |
| No webpage text was copied | Wait for the page, dismiss cookie dialogs, keep Chrome focused |
| Current Weather section not found | Check the URL opened and the page language or layout has not changed |
| Several values show `Not found` | AccuWeather may have changed its labels |
| File saved in an unexpected place | Start PowerShell in this folder first |

# Key takeaways
- Specify each step before writing code — it keeps the bot short and its failures obvious.
- Parse by labels, not positions, when reading text copied from a web page.
- GUI automation is a teaching tool here; a weather API would be the production choice. Not for safety-critical weather decisions.
