import keyboard
import time as t

t.sleep(5)
# keyboard.press_and_release("Menu")
for i in range(40):
    keyboard.press_and_release("Menu")
    t.sleep(1.2)
    for j in range(14):
        keyboard.press_and_release("Down")
        t.sleep(0.05)
    keyboard.press_and_release("Enter")
    t.sleep(0.1)
    keyboard.press_and_release("Down")
    t.sleep(0.2)