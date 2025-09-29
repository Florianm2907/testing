import math
while True:
    stufe = int(input("Stufe: "))
    p = 3
    i = 0
    while i < stufe:
        p = p**3
        i += 1
    print(p)
    datei = open("./faktorial.txt", "w")
    datei.write(str(p))