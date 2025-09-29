import ctypes
import time
import winsound
from pycaw.pycaw import AudioUtilities
from win10toast import ToastNotifier
from playsound import playsound

print("Läuft!")
asdf = False #schon popup geschickt?
play = False #spielt musik?
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
            play = True
        if asdf == False:
            toast = ToastNotifier()
            toast.show_toast("Werbung!", "Spotify Adblocker Version 5.2", duration=5, icon_path="./info.ico")
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
            play = True
        if asdf == False:
            toast = ToastNotifier()
            toast.show_toast("Werbung!", "Spotify Adblocker Version 5.2", duration=5, icon_path="./info.ico")
            asdf = True
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
    time.sleep(1)