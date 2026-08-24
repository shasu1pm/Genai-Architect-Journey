"""Create a dated Excel stock-price report by controlling the desktop.

The bot opens Google Finance in Chrome, copies the visible page text, extracts
Apple's current stock price, enters a five-column report row in Microsoft
Excel, saves the workbook, and takes a screenshot of the final sheet.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import pyautogui
import pyperclip


STOCK_SYMBOL = "AAPL"
EXCHANGE = "NASDAQ"
COMPANY_NAME = "Apple Inc"
STOCK_URL = f"https://www.google.com/finance/quote/{STOCK_SYMBOL}:{EXCHANGE}"
REPORT_COMMENT = "Daily stock price captured automatically."

PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "output"

CHROME_LOCATIONS = (
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
)
EXCEL_LOCATIONS = (
    Path(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"),
    Path(r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"),
)

PAGE_LOAD_SECONDS = 12
APP_LOAD_SECONDS = 8
SAVE_TIMEOUT_SECONDS = 20


def find_installed_app(locations: tuple[Path, ...], app_name: str) -> Path:
    """Return the first installed executable from a list of known locations."""

    for location in locations:
        if location.is_file():
            return location

    raise FileNotFoundError(
        f"{app_name} was not found in the standard installation locations. "
        f"Install {app_name}, or add its executable path to this script."
    )


def wait_for_page_copy(timeout: int = 10) -> str:
    """Wait until Chrome has copied useful Google Finance text."""

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        page_text = pyperclip.paste()
        if STOCK_SYMBOL in page_text and COMPANY_NAME in page_text:
            return page_text
        time.sleep(0.5)

    raise RuntimeError(
        "Google Finance data was not copied. Check the internet connection, "
        "keep Chrome focused, and close any cookie/consent dialog before retrying."
    )


def extract_stock_price(page_text: str) -> str:
    """Extract the primary USD price displayed for Apple on Google Finance."""

    clean_lines = [
        re.sub(r"\s+", " ", line).strip()
        for line in page_text.splitlines()
        if line.strip()
    ]

    try:
        company_line = next(
            index
            for index, line in enumerate(clean_lines)
            if line.casefold() == COMPANY_NAME.casefold()
        )
    except StopIteration as error:
        raise ValueError(f"Could not find {COMPANY_NAME!r} in the copied page.") from error

    # The headline quote appears immediately after the company name. Limiting
    # the search window prevents a related-stock or daily-range value from
    # being mistaken for the current price.
    price_pattern = re.compile(r"^\$\s*\d[\d,]*(?:\.\d{1,4})?$")
    for line in clean_lines[company_line + 1 : company_line + 9]:
        if price_pattern.fullmatch(line):
            return line.replace(" ", "")

    raise ValueError(
        "The current stock price was not found near the company name. "
        "Google Finance may have changed its page layout."
    )


def next_output_paths(captured_at: datetime) -> tuple[Path, Path]:
    """Choose dated filenames without overwriting a previous run."""

    date_text = captured_at.strftime("%Y-%m-%d")
    workbook = OUTPUT_DIR / f"daily_report_{date_text}.xlsx"
    screenshot = OUTPUT_DIR / f"daily_report_{date_text}_screenshot.png"

    if workbook.exists() or screenshot.exists():
        time_text = captured_at.strftime("%H%M%S")
        workbook = OUTPUT_DIR / f"daily_report_{date_text}_{time_text}.xlsx"
        screenshot = OUTPUT_DIR / (
            f"daily_report_{date_text}_{time_text}_screenshot.png"
        )

    return workbook, screenshot


def open_stock_page(chrome_path: Path) -> str:
    """Open Chrome, navigate to the quote page, and copy the visible page."""

    print("1/5 Opening Chrome and Google Finance...")
    subprocess.Popen([str(chrome_path), "--new-window", STOCK_URL])
    time.sleep(PAGE_LOAD_SECONDS)

    # Maximize the active Chrome window and copy the webpage via the keyboard.
    pyautogui.hotkey("win", "up")
    pyautogui.press("esc")
    pyperclip.copy("")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    return wait_for_page_copy()


def activate_excel_window(timeout: int = 15) -> None:
    """Bring an Excel window to the foreground before sending shortcuts."""

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        active_title = pyautogui.getActiveWindowTitle()
        if "excel" in active_title.casefold():
            return

        excel_windows = pyautogui.getWindowsWithTitle("Excel")
        if excel_windows:
            excel_window = excel_windows[-1]
            try:
                if excel_window.isMinimized:
                    excel_window.restore()
                excel_window.activate()
            except Exception:
                # Excel can briefly reject activation while its start screen
                # is loading. The next loop iteration retries safely.
                pass
        time.sleep(0.5)

    raise RuntimeError("Excel opened, but its window could not be activated.")


def workbook_is_active() -> bool:
    """Return whether the foreground Excel window contains a real workbook."""

    return " - excel" in pyautogui.getActiveWindowTitle().casefold()


def wait_for_workbook(timeout: int) -> bool:
    """Wait for Excel to display a worksheet instead of its start screens."""

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if workbook_is_active():
            return True
        time.sleep(0.5)
    return False


def click_blank_workbook_tile() -> None:
    """Click Excel's first template tile relative to the active window."""

    excel_window = pyautogui.getActiveWindow()
    if excel_window is None or "excel" not in excel_window.title.casefold():
        raise RuntimeError("The Excel window lost focus before workbook creation.")

    # The Blank workbook tile is the first large tile on Excel's New page.
    # X scales with the window width; Y stays near the top because Office's
    # template cards have a fixed-height layout. This works for maximized and
    # top-half-snapped Excel windows and avoids hard-coding a screen resolution.
    tile_x = excel_window.left + int(excel_window.width * 0.205)
    tile_y = excel_window.top + min(300, int(excel_window.height * 0.48))
    pyautogui.click(tile_x, tile_y)


def create_blank_workbook(timeout: int = 12) -> None:
    """Leave Excel's Home/New screen and verify that a workbook is active."""

    # Many Excel versions create a workbook with Ctrl+N. Some installations,
    # including the one used for this project, route Ctrl+N to the New page.
    pyautogui.hotkey("ctrl", "n")
    if wait_for_workbook(timeout=4):
        return

    print("     Excel opened the New page; selecting Blank workbook...")
    click_blank_workbook_tile()
    if wait_for_workbook(timeout=timeout):
        return

    raise RuntimeError(
        "Excel did not open a worksheet after the Blank workbook tile was "
        "selected. Ensure Excel is activated and not showing a sign-in dialog."
    )


def open_excel_and_enter_row(
    excel_path: Path,
    captured_at: datetime,
    stock_price: str,
) -> None:
    """Open a blank workbook and paste the required report row."""

    print("3/5 Opening Excel and creating the report row...")
    subprocess.Popen([str(excel_path), "/x"])
    time.sleep(APP_LOAD_SECONDS)
    activate_excel_window()
    pyautogui.hotkey("win", "up")
    create_blank_workbook()
    time.sleep(2)

    timestamp = captured_at.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    stock_data = f"{STOCK_SYMBOL} ({EXCHANGE}): {stock_price} USD"
    table = (
        "Date & Time\tStock Company Name\tStock Data\tSource link\tComment\n"
        f"{timestamp}\t{COMPANY_NAME}\t{stock_data}\t{STOCK_URL}\t"
        f"{REPORT_COMMENT}"
    )

    pyperclip.copy(table)
    pyautogui.hotkey("ctrl", "home")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # Select the populated cells, make the header bold, and auto-fit columns.
    pyautogui.hotkey("ctrl", "home")
    pyautogui.hotkey("ctrl", "shift", "right")
    pyautogui.hotkey("ctrl", "b")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("alt", "h")
    pyautogui.press("o")
    pyautogui.press("i")
    pyautogui.hotkey("ctrl", "home")


def save_workbook(workbook_path: Path) -> None:
    """Use Excel's Save As dialog and wait for the workbook to appear."""

    if not workbook_is_active():
        raise RuntimeError(
            "Cannot save because an Excel workbook is not the active window."
        )

    print(f"4/5 Saving workbook as {workbook_path.name}...")
    pyautogui.press("f12")
    time.sleep(4)
    pyperclip.copy(str(workbook_path))
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    deadline = time.monotonic() + SAVE_TIMEOUT_SECONDS
    submitted_confirmation = False
    while time.monotonic() < deadline:
        if workbook_path.is_file():
            return
        if not submitted_confirmation and time.monotonic() > deadline - 10:
            # Handles a possible Excel format/confirmation dialog.
            pyautogui.press("enter")
            submitted_confirmation = True
        time.sleep(0.5)

    raise RuntimeError(
        f"Excel did not create {workbook_path}. "
        "Complete any visible Save As prompt and run the bot again."
    )


def take_final_screenshot(screenshot_path: Path) -> None:
    """Capture the final, visible Excel sheet using PyAutoGUI."""

    print(f"5/5 Saving screenshot as {screenshot_path.name}...")
    pyautogui.hotkey("win", "up")
    time.sleep(2)
    pyautogui.screenshot(str(screenshot_path))


def run_preflight() -> None:
    """Check the local setup without moving the mouse or typing."""

    chrome_path = find_installed_app(CHROME_LOCATIONS, "Google Chrome")
    excel_path = find_installed_app(EXCEL_LOCATIONS, "Microsoft Excel")
    OUTPUT_DIR.mkdir(exist_ok=True)
    print("Preflight check passed.")
    print(f"Chrome: {chrome_path}")
    print(f"Excel:  {excel_path}")
    print(f"Output: {OUTPUT_DIR}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a stock-price daily report using PyAutoGUI."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="check dependencies and app locations without running automation",
    )
    args = parser.parse_args()

    if args.check:
        run_preflight()
        return 0

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.35
    OUTPUT_DIR.mkdir(exist_ok=True)

    chrome_path = find_installed_app(CHROME_LOCATIONS, "Google Chrome")
    excel_path = find_installed_app(EXCEL_LOCATIONS, "Microsoft Excel")
    captured_at = datetime.now().astimezone()
    workbook_path, screenshot_path = next_output_paths(captured_at)

    print("Starting in 3 seconds. Do not use the mouse or keyboard.")
    print("Move the pointer to the top-left corner for an emergency stop.")
    time.sleep(3)

    page_text = open_stock_page(chrome_path)
    print("2/5 Extracting the current Apple stock price...")
    stock_price = extract_stock_price(page_text)
    print(f"     Captured {STOCK_SYMBOL}: {stock_price} USD")

    open_excel_and_enter_row(excel_path, captured_at, stock_price)
    save_workbook(workbook_path)
    take_final_screenshot(screenshot_path)

    print("\nAutomation completed successfully.")
    print(f"Excel file: {workbook_path}")
    print(f"Screenshot: {screenshot_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except pyautogui.FailSafeException:
        print("\nAutomation stopped by the PyAutoGUI fail-safe.", file=sys.stderr)
        raise SystemExit(2)
    except (FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"\nError: {error}", file=sys.stderr)
        raise SystemExit(1)
