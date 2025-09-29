start = False
zitronentinte = False
benutzername = False
ausdruck = False
asci = False
smiley = False
taschenrechner = False
nichtblinzeln = False
rot13 = False
quiz = False
gemaelde = False

start_freigeschaltet = True 
zitronentinte_freigeschaltet = False
benutzername_freigeschaltet = False
ausdruck_freigeschaltet = False
asci_freigeschaltet = False
smiley_freigeschaltet = False
taschenrechner_freigeschaltet = False
nichtblinzeln_freigeschaltet = False
rot13_freigeschaltet = False
quiz_freigeschaltet = False
gemaelde_freigeschaltet = False

unlocked = ["start"]
solved = []

# while len(solved) <= 11:
#     if "start" in solved:
#         zitronentinte_freigeschaltet = True
#         asci_freigeschaltet = True
#         nichtblinzeln_freigeschaltet = True
#         unlocked.append("zitronentinte")
#         unlocked.append("asci")
#         unlocked.append("nichtblinzeln")

#     if "zitronentinte" in solved:
#         benutzername_freigeschaltet = True
#         ausdruck_freigeschaltet = True
#         unlocked.append("benutzername")
#         unlocked.append("ausdruck")

#     if "asci" in solved:
#         ausdruck_freigeschaltet = True
#         smiley_freigeschaltet = True
#         taschenrechner_freigeschaltet = True
#         unlocked.append("ausdruck")
#         unlocked.append("smiley")
#         unlocked.append("taschenrechner")

#     if "nichtblinzeln" in solved:
#         rot13_freigeschaltet = True
#         quiz_freigeschaltet = True
#         gemaelde_freigeschaltet = True
#         unlocked.append("rot13")
#         unlocked.append("quiz")
#         unlocked.append("gemaelde")

#     if "taschenrechner" in solved:
#         rot13_freigeschaltet = True
#         unlocked.append("rot13")
    
#     # (berechne alle möglichen kombinationen von gelösten und freigeschalteten leveln) 
levels = [
    "start",
    "zitronentinte",
    "benutzername",
    "ausdruck",
    "asci",
    "smiley",
    "taschenrechner",
    "nichtblinzeln",
    "rot13",
    "quiz",
    "gemaelde"
]
solved.append("start")
if "start" in solved:
        zitronentinte_freigeschaltet = True
        asci_freigeschaltet = True
        nichtblinzeln_freigeschaltet = True
        unlocked.append("zitronentinte")
        unlocked.append("asci")
        unlocked.append("nichtblinzeln")

def count_combinations(solved, unlocked):
    if len(solved) == 10:  # Alle Levels wurden gelöst
        return 1

    total_combinations = 0
    if "zitronentinte" in solved:
        benutzername_freigeschaltet = True
        ausdruck_freigeschaltet = True
        unlocked.append("benutzername")
        unlocked.append("ausdruck")

    if "asci" in solved:
        ausdruck_freigeschaltet = True
        smiley_freigeschaltet = True
        taschenrechner_freigeschaltet = True
        unlocked.append("ausdruck")
        unlocked.append("smiley")
        unlocked.append("taschenrechner")

    if "nichtblinzeln" in solved:
        rot13_freigeschaltet = True
        quiz_freigeschaltet = True
        gemaelde_freigeschaltet = True
        unlocked.append("rot13")
        unlocked.append("quiz")
        unlocked.append("gemaelde")

    if "taschenrechner" in solved:
        rot13_freigeschaltet = True
        unlocked.append("rot13")
    for level in unlocked:
        if level not in solved and globals()[f"{level}_freigeschaltet"]:
            solved.append(level)
            unlocked.remove(level)
            total_combinations += count_combinations(solved, unlocked)
            unlocked.append(level)
            solved.remove(level)

    return total_combinations

# Starte die Berechnung der Kombinationen
total = count_combinations(solved, unlocked)
print("Die Gesamtanzahl der möglichen Kombinationen ist:", total)
print(solved)