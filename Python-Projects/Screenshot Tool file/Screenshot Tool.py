# Screenshot Tool

import pyautogui
import datetime

def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_name)
    print(f"Screenshot saved as {screenshot_name}")

# Test the Screenshot Tool
take_screenshot()


'''
=================================
Test Case:
=================================

Screenshot saved as screenshot_2023-06-26_06-10-26.png

'''