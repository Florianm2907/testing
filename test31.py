from PIL import ImageGrab
import time as t

t.sleep(5)
px = ImageGrab.grab().load()
color = px[741, 443]
print(color)
print(color[1])