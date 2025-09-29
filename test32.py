import mouse
import time as t
from PIL import ImageGrab
run = False
t.sleep(2)
while True:
    px = ImageGrab.grab().load()
    color = px[749, 474]
    if color[0] == 50: run = True
    if run:
        mouse.move(703, 550, absolute=True)
        for i in range(4):
            mouse.click()
            mouse.move(20, 0, absolute=False)
            mouse.click()
            mouse.move(20, 0, absolute=False)
            mouse.click()
            mouse.move(20, -20, absolute=False)
            mouse.click()
            mouse.move(20, 20, absolute=False)
            mouse.click()
            mouse.move(20, 0, absolute=False)
            mouse.click()
            mouse.move(20, 0, absolute=False)
        for i in range(3):
            mouse.click() 
            mouse.move(20, 0, absolute=False)
        mouse.click()
        run = False
        t.sleep(0.5)