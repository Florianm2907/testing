import win32gui
tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
import time
while True:
    print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    # if (tempWindowName==win32gui.GetWindowText (win32gui.GetForegroundWindow())):
    #     pass
    # else:
    #     tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
    #     #do what you want
    time.sleep(0.1)