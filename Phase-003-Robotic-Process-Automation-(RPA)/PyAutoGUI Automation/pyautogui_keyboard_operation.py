import time
import pyautogui

# Give yourself 5 seconds to switch to the target application
print("Switch to Notepad within 5 seconds...")
time.sleep(5)

# Type text
pyautogui.write("Hello World", interval=0.1)

# Select all
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)

# Copy
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Move to a new line
pyautogui.press("enter")
time.sleep(0.5)

# Paste
pyautogui.hotkey("ctrl", "v")