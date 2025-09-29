import time as t
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

while True:
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Alexa.exe":
            volume.SetMasterVolume(.2, None)
            print("hier")
