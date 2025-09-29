import mouse
import time as t
from PIL import ImageGrab

run = False
t.sleep(5)
while True:
    px = ImageGrab.grab().load()
    color = px[748, 451]
    if color[0] == 50: run = True
    if run:
        mouse.move(703, 551, absolute=True)
        for i in range(28):
            mouse.click()
            mouse.move(20, 0, absolute=False)
        run = False
        t.sleep(0.5)