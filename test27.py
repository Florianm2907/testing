from pynput.keyboard import *
from pynput.mouse import *
import time as t
import pyautogui

delay = 0.5  # in seconds
pause_key = Key.f2

keyboard = Controller()
mouse = Controller()

pause = True
running = True
def on_press(key):
    global running, pause
    if key == pause_key:
        if pause: pause = False
        else:
            pause = True
            print("pause")
def main():
    lis = Listener(on_press=on_press)
    lis.start()
    while running:
        if not pause:
            pyautogui.scroll(-10)
            t.sleep(delay)
    lis.stop()
if __name__ == "__main__":
    main()