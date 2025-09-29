from pydub import AudioSegment
import glob
import os

# oggs = []
# for file in glob.glob(r'C:/Users/Florian/Downloads/Developer.Art.Classic.v1.18.2_3/assets/minecraft/sounds/**/*.ogg', recursive=True):
#     oggs.append(file)
# # print(oggs)
# print(len(oggs))
# i=0

# print(oggs[0][83::])
# for x in oggs:
#     song = AudioSegment.from_ogg(x)
#     neu = song + 10
#     audiopath = r"C:\Users\Florian\Desktop\Soundpack\sounds//" + oggs[i][83::]
#     neu.export(audiopath, format="ogg")
#     i+=1
#     print(x + "wurde als " + audiopath + " exportiert.")
song = AudioSegment.from_mp3(r"C:\Users\Florian\Downloads\MagnusTheMagnus - Area.mp3")
neu = song+10
neu.export(r"C:/Users/Florian/Desktop/test.mp3", format="mp3")