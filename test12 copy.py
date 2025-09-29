from pydub import AudioSegment
import glob

pathzumurspruenglichenpack = r'C:\Users\Florian\Downloads\Pack\assets\minecraft'
pathzumneuenpack = r"C:/Users/Florian/Desktop/Soundpack/"
lautst = 25

oggs = []
soundpack = pathzumurspruenglichenpack + '/**/*.ogg'
for file in glob.glob(soundpack, recursive=True):
    oggs.append(file)
i=0
for x in oggs:
    song = AudioSegment.from_ogg(x)
    neu = song + lautst
    if len(oggs[i].split("\\")) == 9:
        audiopath = pathzumneuenpack + oggs[i].split("\\")[-2] + "/" + oggs[i].split("\\")[-1]
    else:
        audiopath = pathzumneuenpack
        for j in range(len(oggs[i].split("\\"))-8,0,-1):
            audiopath+=oggs[i].split("\\")[-(j+1)]
            audiopath+="/"
        audiopath+= oggs[i].split("\\")[-1]
    print(audiopath)
    neu.export(audiopath, format="ogg")
    i+=1
    print(x + " wurde als " + audiopath + " exportiert.")
print("Fertig.")