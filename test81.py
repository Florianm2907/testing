import time as t
import pyautogui

t.sleep(5)
while True:
    pyautogui.moveTo(200, 400, duration=0.4)
    t.sleep(0.2)
    pyautogui.moveTo(2300, 400, duration=0.4)
    t.sleep(0.2)
    pyautogui.moveTo(2300, 1100, duration=0.4)
    t.sleep(0.2)
    pyautogui.moveTo(200, 1100, duration=0.4)
    t.sleep(0.2)
