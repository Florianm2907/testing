from genericpath import isfile
import os
import time as t

a=3
def mal(a):
    a = a*a*a
    return a
os.remove("./grahamsnumber.txt")
while True:
    datei = open("./grahamsnumber.txt", "w")
    a=3
    potenz = input(r"Potenz: ")
    dauer = t.time()
    for h in range(int(potenz)):
        # print(mal(a))
        a=mal(a)
        print("Stufe", h+1, "wird berechnet...")
    # print(a)
    print("Fast fertig")
    datei.write(str(a))
    print("Fertig")
    # t.sleep(50)
    print(t.time() - dauer)
    datei.close()
    os.system("grahamsnumber.txt")