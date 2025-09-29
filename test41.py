from pynput.keyboard import *
from pynput.mouse import *
import time as t
import pyautogui
pause_key = Key.ctrl_l

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
            print("wo")
            pyautogui.leftClick()
            t.sleep(10)
        else:
            print("hi")
    lis.stop()
if __name__ == "__main__":
    main()