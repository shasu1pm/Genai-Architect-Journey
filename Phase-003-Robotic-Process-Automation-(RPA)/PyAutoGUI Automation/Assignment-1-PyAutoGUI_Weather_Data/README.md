# Bengaluru Weather Bot

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

A Windows desktop automation bot that opens AccuWeather in Google Chrome, copies the visible page text, extracts Bengaluru's current weather, pastes a formatted report into Notepad, and saves it with a date-based filename.

📄 **Project document:** [Bengaluru Weather Bot.pdf](./Bengaluru%20Weather%20Bot.pdf)

## Workflow

```text
Launch Chrome → open AccuWeather → copy page text → parse current weather
→ open Notepad → paste formatted data → save YYYY-MM-DD_Weather_Data.txt
```

The report can contain temperature, RealFeel, condition, wind, gusts, humidity, indoor humidity, dew point, pressure, cloud cover, visibility, cloud ceiling, capture time, and source URL. When a value cannot be identified, the script records `Not found`.

## Requirements

- Windows 10 or Windows 11
- Python 3.10+
- Google Chrome in a standard installation location or available on `PATH`
- Internet access

## Setup

```powershell
cd "PyAutoGUI Automation\Assignment-1-PyAutoGUI_Weather_Data"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pyautogui pyperclip pillow
```

## Run

Close or minimize unrelated windows, keep the terminal visible, and run:

```powershell
python Assignment1_Weather_Data.py
```

Do not touch the mouse or keyboard while the bot is working. To trigger PyAutoGUI's emergency stop, quickly move the pointer to the upper-left corner of the primary display.

## Output

The bot saves the report in the current working directory:

```text
YYYY-MM-DD_Weather_Data.txt
```

Existing dated `.txt` files and the screen recording in this folder are sample assignment artifacts. Running the bot again on the same date may replace that date's file after interacting with Notepad's overwrite dialog.

## How this bot was specified

The automation was written from a deliberately precise specification. Stating each
step, and the constraints around it, before writing any code is what kept the
implementation short and made the failure cases obvious:

| Step | Requirement |
| :-- | :-- |
| 1 | Open the Chrome browser |
| 2 | Open the AccuWeather Bengaluru current-weather page in a new tab |
| 3 | Copy the **values** inside the Current Weather section — not merely the heading text |
| 4 | Open Notepad and start a new document |
| 5 | Paste the parsed weather data |
| 6 | Save as `{Today Date}_Weather_Data.txt` in the project folder |

Three constraints shaped the design:

- Chrome must stay **visible and focused** while the page is being copied, because
  PyAutoGUI sends shortcuts to whichever window currently has focus.
- The desktop must be left alone during a run — moving the pointer to the
  top-left corner triggers PyAutoGUI's emergency stop.
- `hotkey()` handles the `Ctrl+C` / `Ctrl+V` shortcuts, while **Pyperclip** reads
  and writes the plain text through the Windows clipboard.

Step 3 is the one that carries all the difficulty. Copying the page is trivial;
identifying which of the copied lines are the current readings is the actual
work, and it is why the parser is written around labelled regular expressions
rather than fixed line offsets.

## Configuration

The following values are defined near the top of `Assignment1_Weather_Data.py`:

- `WEATHER_URL` selects the AccuWeather location and page.
- `PROJECT_FOLDER = os.getcwd()` means output is written to the directory from which Python is launched, not necessarily the script's directory.
- The 15-second page-load sleep can be increased in the script for slower connections.

The parsing patterns are designed for AccuWeather's English Bengaluru current-weather page. A different location, language, unit system, or page layout may require updates to the regular expressions.

## Troubleshooting

- **No webpage text was copied:** wait for the page to finish loading, dismiss cookie or consent dialogs, and make sure Chrome is focused.
- **Current Weather section was not found:** verify that the configured URL opened and that the page language/layout has not changed.
- **Several values show `Not found`:** AccuWeather may have changed its labels or formatting.
- **File is saved in an unexpected place:** start PowerShell in this folder before running the script.
- **Actions occur in the wrong application:** close extra Chrome/Notepad windows and rerun without changing focus.

## Limitations

This project intentionally demonstrates GUI automation. It is more sensitive to focus and page layout than an API-based weather integration, and it should not be used as a source for safety-critical weather decisions.

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
