import ctypes
import time as t
import winsound
import psutil
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from win10toast import ToastNotifier
from playsound import playsound

version = "5.6"

print("Läuft!")
# toast = ToastNotifier()
# toast.show_toast("Adblocker läuft!", "Spotify Adblocker Version " + version, duration=5, icon_path="./info.ico")
asdf = False #schon popup geschickt?
play = False #spielt musik?
maxVolume = 10

def wirdausgefuehrt(procName):
    for proc in psutil.process_iter():
        try:
            if procName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

# lautst. von python auf den Wert "vol" setzen
def audio(vol):
    lautst = vol/100
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "adblockv.5.6.exe" or session.Process and session.Process.name() == "python.exe":
            volume.SetMasterVolume(lautst, None)

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
    if not wirdausgefuehrt("Spotify.exe"): print("Spotify nicht gefunden!")
    elif "Advertisement" in titles:
        print("Werbung!")
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == "Spotify.exe":
                volume = session.SimpleAudioVolume
                volume.SetMute(1, None)
        if not play:
            winsound.PlaySound(r'H:\test1\ad-blocking\wartemusik.wav', winsound.SND_ASYNC)
            for i in range(maxVolume):
                audio(i)
                t.sleep(.1)
            play = True
        if asdf == False:
            toast = ToastNotifier()
            toast.show_toast("Werbung!", "Spotify Adblocker Version " + version, duration=3, icon_path="./info.ico")
            asdf = True
    elif "Spotify" in titles:
        print("Werbung!")
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == "Spotify.exe":
                volume = session.SimpleAudioVolume
                volume.SetMute(1, None)
        if not play:
            winsound.PlaySound(r'H:\test1\ad-blocking\wartemusik.wav', winsound.SND_ASYNC)
            for i in range(maxVolume):
                audio(i)
                t.sleep(.1)
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
            for i in range(maxVolume):
                audio(maxVolume+1-i)
                t.sleep(.02)
            winsound.PlaySound(None, winsound.SND_PURGE)
            play = False
    t.sleep(1)