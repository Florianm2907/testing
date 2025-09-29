from random import random, randrange
from pynput.keyboard import *
import pyautogui
import time as t

pause_key = Key.ctrl_r
exit_key = Key.esc
running = True
pause = False
mouse = Controller()

def on_press(key):
    global running, pause
    if key == pause_key:
        if pause:
            pause = False
            print("[Weiter]")
        else:
            pause = True
            print("[Pausiert]")
    elif key == exit_key:
        running = False
def main():
    lis = Listener(on_press=on_press)
    lis.start()
    while running:
        if not pause:
            x = randrange(-5, 5)
            y = randrange(-5, 5)
            pyautogui.move(x, y)
            t.sleep(.1)
    lis.stop()
if __name__ == "__main__":
    main()