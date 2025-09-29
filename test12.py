from pydub import AudioSegment
import os

meinpath = r"C:\Users\Florian\Downloads\Developer.Art.Classic.v1.18.2_3\assets\minecraft\sounds"
path = []
oggs = []
for x in os.listdir(meinpath):
    if not ".ogg" in x:
        path.append(x)
    else: oggs.append(x)
for y in path:
    if not ".ogg" in y:
        print(path)
        print(oggs)
        for z in os.listdir(meinpath+"\\"+y):
            if not ".ogg" in z:
                path.append(z)
            else:
                oggs.append(z)
    else:
        oggs.append(y)
print(path)
print(oggs)
#song = AudioSegment.from_ogg()