oggs = ["C:\\Users\\Florian\\Downloads\\Pack\\assets\\minecraft\\sound\\ambient\\cave\\cave1.ogg"]

audiopath = r"C:/Users/Florian/Desktop/Soundpack/"
for j in range(len(oggs[0].split("\\"))-8,0,-1):
    audiopath+=oggs[0].split("\\")[-(j+1)]
    audiopath+="/"
audiopath+= oggs[0].split("\\")[-1]
print(audiopath)