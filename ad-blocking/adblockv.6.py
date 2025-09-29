import ctypes
import time as t
import tkinter as tk
import winsound
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from win10toast import ToastNotifier
from playsound import playsound
from tkinter import ttk
from tkinter.messagebox import showinfo
from swinlnk.swinlnk import SWinLnk

version = "6"

root = tk.Tk()
root.title('Spotify Adblock v.6')
root.geometry('300x300+50+50')
root.resizable(False, False)
root.attributes('-alpha', 0.9)
message = tk.Label(root, text = "Das ist ein Test")
message.pack()
check = tk.StringVar() # checkbox
ttk.Checkbutton(root,
                text='Automatisch starten',
                command=None,
                variable=check,
                onvalue='an',
                offvalue='aus').pack()
root.mainloop()

print("Läuft!")
toast = ToastNotifier()
toast.show_toast("Adblocker läuft!", "Spotify Adblocker Version " + version, duration=5, icon_path="./info.ico")
asdf = False # schon popup geschickt?
play = False # spielt musik?

# lautst. von python auf 20% setzen
def audio():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        program = "adblockv." + version + ".exe"
        if session.Process and session.Process.name() == program:
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(0.2, None)

while True:
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows = ctypes.windll.user32.EnumWindows    
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    titles = []
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    if "Advertisement" in titles:
        sessions = AudioUtilities.GetAllSessions()
        print("Werbung!")
        for session in sessions:
            if session.Process and session.Process.name() == "Spotify.exe":
                volume = session.SimpleAudioVolume
                volume.SetMute(1, None)
        if not play:
            winsound.PlaySound(r'H:\test1\ad-blocking\wartemusik.wav', winsound.SND_ASYNC)
            audio()
            play = True
        if asdf == False:
            toast = ToastNotifier()
            toast.show_toast("Werbung!", "Spotify Adblocker Version " + version, duration=3, icon_path="./info.ico")
            asdf = True
    elif "Spotify" in titles:
        sessions = AudioUtilities.GetAllSessions()
        print("Werbung!")
        for session in sessions:
            if session.Process and session.Process.name() == "Spotify.exe":
                volume = session.SimpleAudioVolume
                volume.SetMute(1, None)
        if not play:
            winsound.PlaySound(r'H:\test1\ad-blocking\wartemusik.wav', winsound.SND_ASYNC)
            audio()
            play = True
        if asdf == False:
            toast = ToastNotifier()
            toast.show_toast("Werbung!", "Spotify Adblocker Version " + version, duration=5, icon_path="./info.ico")
            asdf = True
    elif "Spotify Free" in titles:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == "Spotify.exe":
                volume = session.SimpleAudioVolume
                volume.SetMute(1, None)
    else:
        asdf = False
        print("Keine Werbung!")
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            volume.SetMute(0, None)
        if play:
            winsound.PlaySound(None, winsound.SND_PURGE)
            play = False
    t.sleep(1)