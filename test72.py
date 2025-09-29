import mouse
import time as t
import keyboard as k
import tkinter as tk
from pynput.mouse import Controller
import pyautogui
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
run = True
excluded_range_x = range(0, 151)
excluded_range_y = range(0, 151)
m = Controller()
t.sleep(2)
mouse.move(0,0)
while run:
    for y in range(150, height, 10):
        for x in range(150, width, 10):
            # mouse.move(x,y,absolute=True, duration=0, steps_per_second=120.0)
            # pyautogui.move(x,y)
            # m.position = (x,y)
            m.move(x,y)
            mouse.click()
            if k.is_pressed("a"):
                run = False
                break
                