import os
import shutil
from winotify import Notification, audio
import time as t
# shutil.copy("./BEWERBUNG.exe", "%USERPROFILE%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
# os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
while True:
    toast = Notification(app_id="Microsoft Windows",
                        title="Es wurde ein Virus erkannt!",
                        msg="Es wurde ein Virus erkannt! Hier ist der Link um ihn zu beseitigen:"
                        )
    toast.add_actions(label="Klicke hier", 
                  launch="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    toast.set_audio(audio.Mail ,loop=True)
    toast.show()
    t.sleep(5)
    # alarm 6
    # alarm 9
    # alarm 10