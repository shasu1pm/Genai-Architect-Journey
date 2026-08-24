import os
import re
import subprocess
import time
from datetime import datetime

import pyautogui
import pyperclip


WEATHER_URL = (
    "https://www.accuweather.com/en/in/bengaluru/"
    "204108/current-weather/204108"
)

# The text file will be saved in the folder from which this script is run.
PROJECT_FOLDER = os.getcwd()


def open_chrome() -> None:
    """Open Google Chrome on Windows 11."""

    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for chrome_path in chrome_paths:
        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path])
            return

    # Fallback when Chrome is available through the Windows PATH.
    subprocess.Popen(["cmd", "/c", "start", "chrome"], shell=True)


def clean_text(text: str) -> str:
    """Remove blank lines and unnecessary spaces."""

    lines = []

    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line).strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


def find_value(
    text: str,
    pattern: str,
    default: str = "Not found",
) -> str:
    """Find the first matching value from the copied webpage text."""

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    if match:
        return match.group(1).strip()

    return default


def extract_current_weather(page_text: str) -> str:
    """
    Extract the actual weather values from the
    Current Weather section.
    """

    text = clean_text(page_text)

    # Start from the Current Weather heading.
    start_position = text.lower().find("current weather")

    if start_position == -1:
        raise ValueError(
            "The 'Current Weather' section was not found."
        )

    weather_section = text[start_position:]

    # Stop before unrelated sections.
    ending_headings = [
        "hourly weather",
        "daily weather",
        "weather radar",
        "looking ahead",
        "air quality",
        "today's weather",
    ]

    section_end = len(weather_section)

    for heading in ending_headings:
        position = weather_section.lower().find(heading, 20)

        if position != -1:
            section_end = min(section_end, position)

    weather_section = weather_section[:section_end]

    temperature = find_value(
        weather_section,
        r"\b(\d{1,2}\s*°\s*C)\b",
    )

    realfeel = find_value(
        weather_section,
        r"RealFeel(?:®|™)?\s*(\d{1,2}\s*°?\s*C?)",
    )

    condition = find_value(
        weather_section,
        (
            r"\n("
            r"Mostly cloudy|Partly cloudy|Cloudy|Clear|Sunny|"
            r"Mostly sunny|Partly sunny|Overcast|Light rain|"
            r"Rain|Showers|Thunderstorm|Fog|Hazy|Windy"
            r")\n"
        ),
    )

    wind = find_value(
        weather_section,
        r"\bWind\s*\n?([NSEW]{1,3}\s+\d+(?:\.\d+)?\s*km/h)",
    )

    wind_gusts = find_value(
        weather_section,
        r"Wind Gusts\s*\n?(\d+(?:\.\d+)?\s*km/h)",
    )

    humidity = find_value(
        weather_section,
        r"(?<!Indoor )Humidity\s*\n?(\d+\s*%)",
    )

    indoor_humidity = find_value(
        weather_section,
        r"Indoor Humidity\s*\n?([^\n]+)",
    )

    dew_point = find_value(
        weather_section,
        r"Dew Point\s*\n?(\d+(?:\.\d+)?\s*°?\s*C)",
    )

    pressure = find_value(
        weather_section,
        r"Pressure\s*\n?(?:↑|↓)?\s*(\d+(?:\.\d+)?\s*mb)",
    )

    cloud_cover = find_value(
        weather_section,
        r"Cloud Cover\s*\n?(\d+\s*%)",
    )

    visibility = find_value(
        weather_section,
        r"Visibility\s*\n?(\d+(?:\.\d+)?\s*km)",
    )

    cloud_ceiling = find_value(
        weather_section,
        r"Cloud Ceiling\s*\n?(\d[\d,]*\s*m)",
    )

    captured_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    return f"""CURRENT WEATHER - BENGALURU
========================================

Captured Date and Time : {captured_time}

Temperature            : {temperature}
RealFeel                : {realfeel}
Condition               : {condition}

Wind                    : {wind}
Wind Gusts              : {wind_gusts}
Humidity                : {humidity}
Indoor Humidity         : {indoor_humidity}
Dew Point               : {dew_point}

Pressure                : {pressure}
Cloud Cover             : {cloud_cover}
Visibility              : {visibility}
Cloud Ceiling           : {cloud_ceiling}

Source:
{WEATHER_URL}
"""


def save_notepad_file(file_path: str) -> None:
    """Save the active Notepad tab using the required filename."""

    pyautogui.hotkey("ctrl", "shift", "s")
    time.sleep(2)

    # Enter the full path in the Save As dialog.
    pyperclip.copy(file_path)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(3)

    # Confirm replacement if the file already exists.
    if pyautogui.press:
        pyautogui.press("left")
        pyautogui.press("enter")


def main() -> None:
    # Move the mouse to the top-left corner to stop the automation.
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5

    today_date = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{today_date}_Weather_Data.txt"
    file_path = os.path.join(PROJECT_FOLDER, file_name)

    print("Step 1: Opening Chrome...")
    open_chrome()
    time.sleep(5)

    print("Step 2: Opening AccuWeather in a new tab...")
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)

    pyperclip.copy(WEATHER_URL)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    # Increase this delay if the internet connection is slow.
    time.sleep(15)

    print("Step 3: Copying the Current Weather data...")

    # Click inside the webpage before selecting the page text.
    pyautogui.click(700, 500)
    time.sleep(1)

    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)

    page_text = pyperclip.paste()

    if not page_text.strip():
        raise RuntimeError(
            "No webpage text was copied. Check whether the page loaded."
        )

    weather_data = extract_current_weather(page_text)

    print("Weather data extracted successfully:")
    print(weather_data)

    print("Step 4: Opening Windows 11 Notepad...")
    subprocess.Popen(["notepad.exe"])
    time.sleep(4)

    # Open a new Notepad tab.
    pyautogui.hotkey("ctrl", "n")
    time.sleep(2)

    print("Step 5: Pasting the weather data...")
    pyperclip.copy(weather_data)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)

    print("Step 6: Saving the weather file...")
    save_notepad_file(file_path)

    print("Automation completed successfully.")
    print(f"Saved file: {file_path}")


if __name__ == "__main__":
    try:
        main()

    except pyautogui.FailSafeException:
        print(
            "Automation stopped because the mouse was moved "
            "to the top-left corner."
        )

    except Exception as error:
        print(f"Automation failed: {error}")