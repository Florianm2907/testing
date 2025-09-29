import time as t
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def audio(vol):
    lautst = vol/100
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            volume.SetMasterVolume(lautst, None)
    print(lautst)
while True:
    for i in range(20):
        audio(21-i)
        t.sleep(.05)