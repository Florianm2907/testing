import os
a = []
b = []
c = 0
while True:
    a.append(c)
    for i in range(len(a)):
        b.append(a[i])
    c+=1
    print(c)
    if c == 50000:
        print(len(b))
        break
        # datei = open("./iwas.txt", "w")
        # datei.write(str(b))
        # datei.close()
        # os.system("iwas.txt")