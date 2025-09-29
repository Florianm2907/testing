import time as t
import random
text = "According to all known laws of aviation, there is no way a bee should be able to fly. It's wings are too small to get it's fat little body off the ground."
temp = ""
def einzeln(text):
    temp = ""
    for i in range(len(text)):
        for j in range(32, ord(text[i])):
            print(temp + chr(j))
            t.sleep(0.005)
        temp += text[i]
    print(temp)

def alles(text):
    temp = ""
    for i in range(len(text)):
        for j in range(32, ord(text[i])):
            print(temp + chr(j) + chr(j) * (len(text) - len(temp) - 1))
            t.sleep(0.0005)
        temp += text[i]
    print(f"\n{temp}")

einzeln(text)
# alles(text)
# for i in range(3, 4, 2):
#     text = "text"
#     print(text[i], end="!")

# eingabe = "hallodasisttext"
# for x in range(len(eingabe)):
#     temp = eingabe[len(eingabe)-1-x]
#     print(temp)
# if "TEXT".isupper: print("hallo")
# var = "TEXT"
# if var.isupper: print("jeztzuasdas")
# lexikon = ["Chris", "liebt", "Alex"]
# outputs = []
# for i in range(5):
#     x = random.sample(lexikon, 3)
#     if not x in outputs: print(x)
#     else: print("(Wiederholung)")
#     outputs.append(x)

# liste = {"modern":"Adjektiv"}
# liste.update({"essen":"Verb"})
# print(liste)

# woerter_und_wortarten = {"modern": "Adjektiv", "essen": "Verb", "Essen": "Eigenname"}
# neue_woerter = ["Star", "starren"]
# neue_wortarten = ["Nomen", "Verb"]
# for i in range(len(neue_woerter)):
#     woerter_und_wortarten.update({neue_woerter[i]: neue_wortarten[i]})
# print(woerter_und_wortarten)
# print(sorted(woerter_und_wortarten.items()))
# for wort, wortart in woerter_und_wortarten.items():
#     print(f"{wort}: {wortart}")