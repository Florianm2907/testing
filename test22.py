from tkinter import Tk
import keyboard as k
muted = False
while True:
    if k.is_pressed("Ctrl+AltGr+M"):
        if muted:
            win = Tk()
            win.geometry("15x15")
            win.overrideredirect(True)
            win.wm_attributes("-topmost", 1)
            win.attributes('-alpha', 0.5)
            win.configure(bg='#00ff00')
            win.update()
            muted = False
        else:
            win = Tk()
            win.geometry("15x15")
            win.overrideredirect(True)
            win.wm_attributes("-topmost", 1)
            win.attributes('-alpha', 0.5)
            win.configure(bg='#ff0000')
            win.update()
            muted = True