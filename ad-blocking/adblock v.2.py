from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import win32gui
import time

print("Läuft!")
def mute():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            #print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(0, None)

def unmute():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            #print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(1, None)



while True:
    abcd = ""
    def winEnumHandler( hwnd, ctx ):
            if win32gui.IsWindowVisible( hwnd ):
                offen = (win32gui.GetWindowText( hwnd ))
                # for i in range(len(offen)):
                #     if not "-" in offen[i]:
                #         offen = ""
                if "Advertisement" in offen:
                    print("Werbung!")
                    mute()
                    time.sleep(2)
                else:
                    offen = ""
                    unmute()
                
                # else:
                #     print("Keine Werbung!")
                #     unmute()
    win32gui.EnumWindows( winEnumHandler, None )
    time.sleep(0)