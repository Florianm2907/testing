import pyautogui as gui
import time as t
import keyboard as k

asd = True
k.wait('ctrl')
while asd:
    # gui.scroll(50)
    # gui.click()
    gui.dragRel(0, -500, duration=1)
    gui.scroll(10)
    gui.scroll(-10)
    # gui.dragRel(0, 1, duration=0.3)
    # gui.dragRel(0, -1, duration=0.3)
    # gui.click(clicks=2, interval=0.1)
    # gui.mouseDown(button='left')
    # t.sleep(0.2)
    # gui.mouseUp(button='left')
    # gui.dragRel(0, 10, duration=0.1)
    # gui.dragRel(0, -10, duration=0.1)
    gui.moveRel(0, 500)
    t.sleep(.5)
    if k.is_pressed('shift'): 
        asd = False