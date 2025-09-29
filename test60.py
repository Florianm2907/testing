import math
from decimal import Decimal, getcontext

radius = 6374340
distanz = 87654321

def schwerkraft_stärke(distanz):
    G = 6.67430 * 10**(-11)
    M1 = (9.81*(6374340**2)/G)
    r = distanz + radius
    g = G * (M1 / r**2)
    return g

def beschleunigung(beschl, schwerkr):
    v = math.sqrt(beschl**2 + 2 * schwerkr * 1)
    return v

def berechne_zeit(distanz):
    aktuelle_beschl = 0
    aktuelle_dist = distanz
    zeit = 0
    for t in range(distanz):
        zeit_schritt = (beschleunigung(aktuelle_beschl, schwerkraft_stärke(aktuelle_dist)) - aktuelle_beschl) / schwerkraft_stärke(aktuelle_dist)
        zeit += zeit_schritt
        aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(aktuelle_dist)) #- aktuelle_beschl / schwerkraft_stärke(aktuelle_dist)
        if aktuelle_dist > 1000000: 
            aktuelle_dist -= 1000000
            t += 1000000
        elif aktuelle_dist > 1000: 
            aktuelle_dist -= 1000
            t += 1000
        else: aktuelle_dist -= 1 
        if t % 1000000 == 0:
            print(aktuelle_dist)
            print(aktuelle_beschl)
            print(zeit)
    return zeit

print(f"Zeit: {berechne_zeit(distanz)}")

# def berechne_hoehe(zeit):
#     aktuelle_beschl = Decimal('0')
#     aktuelle_dist = Decimal('0')  # Starte bei der Oberfläche der Erde
#     aktuelle_zeit = Decimal('0')
#     getcontext().prec = 28  # Präzision für Dezimalzahlen

#     while aktuelle_zeit < zeit:
#         aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(radius + aktuelle_dist))
#         zeit_schritt = aktuelle_beschl / schwerkraft_stärke(radius + aktuelle_dist)
#         aktuelle_zeit += zeit_schritt
#         aktuelle_dist += Decimal('1')

#     return aktuelle_dist

# gesuchte_zeit = Decimal('755367.5351298475669')  # Beispiel für eine Zeit mit vielen Nachkommastellen
# hoehe = berechne_hoehe(gesuchte_zeit)
# print(hoehe)
# # def berechne_distanz(zeit):
# #     aktuelle_distanz = 0
# #     aktuelle_beschl = 0
# #     return

# # # # import math

# # # # radius = 6374340

# # # # def schwerkraft_stärke(distanz):
# # # #     G = 6.67430 * 10**(-11)
# # # #     M1 = (9.81 * (radius**2) / G)
# # # #     r = distanz + radius
# # # #     g = G * (M1 / r**2)
# # # #     return g

# # # # def beschleunigung(beschl, schwerkr):
# # # #     v = math.sqrt(beschl**2 + 2 * schwerkr * 1)
# # # #     return v

# # # # def berechne_distanz(zeit):
# # # #     aktuelle_beschl = 0
# # # #     aktuelle_dist = 0
# # # #     zeit_schritt = 0.0000000000001  # Zeit-Schrittgröße
# # # #     while zeit > 0:
# # # #         aktuelle_beschl = schwerkraft_stärke(aktuelle_dist)
# # # #         v = beschleunigung(aktuelle_beschl, aktuelle_beschl)
# # # #         aktuelle_dist += v * zeit_schritt
# # # #         zeit -= zeit_schritt
# # # #         if zeit == 1: print("hier")
# # # #     return aktuelle_dist

# # # # gegebene_zeit = 755367.5351298475669  # Zeit in Sekunden (zum Beispiel 100 Sekunden)
# # # # resultierende_distanz = berechne_distanz(gegebene_zeit)
# # # # print(f"Gefallene Distanz in {gegebene_zeit} Sekunden: {resultierende_distanz} Meter")

# # import math

# # radius = 6374340

# # def schwerkraft_stärke(distanz):
# #     G = 6.67430 * 10**(-11)
# #     M1 = (9.81 * (radius**2) / G)
# #     r = distanz + radius
# #     g = G * (M1 / r**2)
# #     return g

# # def berechne_distanz(zeit):
# #     G = 6.67430 * 10**(-11)
# #     M1 = (9.81 * (radius**2) / G)
# #     r = radius
# #     aktuelle_beschl = G * (M1 / r**2)
# #     aktuelle_dist = 0
# #     zeit_schritt = 1  # Zeit-Schrittgröße
# #     v = 0

# #     while zeit > 0:
# #         v += aktuelle_beschl * zeit_schritt
# #         aktuelle_dist += v * zeit_schritt
# #         zeit -= zeit_schritt
# #     return aktuelle_dist

# # gegebene_zeit = 755367.5351298475669  # Zeit in Sekunden (zum Beispiel 100 Sekunden)
# # resultierende_distanz = berechne_distanz(gegebene_zeit)
# # print(f"Gefallene Distanz in {gegebene_zeit} Sekunden: {resultierende_distanz} Meter")


# # # import math
# # # import threading

# # # radius = 6374340
# # # G = 6.67430 * 10**(-11)
# # # M1 = (9.81 * (radius**2) / G)
# # # r = radius
# # # aktuelle_beschl = G * (M1 / r**2)

# # # def schwerkraft_stärke(distanz):
# # #     r = distanz + radius
# # #     g = G * (M1 / r**2)
# # #     return g

# # # def berechne_distanz(zeit, thread_id, result):
# # #     v = 0
# # #     aktuelle_dist = 0
# # #     zeit_schritt = 0.0001  # Zeit-Schrittgröße

# # #     while zeit > 0:
# # #         v += aktuelle_beschl * zeit_schritt
# # #         aktuelle_dist += v * zeit_schritt
# # #         zeit -= zeit_schritt

# # #     result[thread_id] = aktuelle_dist

# # # gegebene_zeit = 755367.5351298475669  # Zeit in Sekunden (zum Beispiel 100 Sekunden)
# # # num_threads = 24  # Anzahl der Threads

# # # # Erstellen von Threads und Ergebnis-Arrays
# # # threads = []
# # # results = [0] * num_threads

# # # # Starten der Threads
# # # for i in range(num_threads):
# # #     t = threading.Thread(target=berechne_distanz, args=(gegebene_zeit, i, results))
# # #     threads.append(t)
# # #     t.start()

# # # # Warten auf das Ende aller Threads
# # # for t in threads:
# # #     t.join()

# # # # Summieren der Ergebnisse aus den Threads
# # # resultierende_distanz = sum(results)
# # # print(f"Gefallene Distanz in {gegebene_zeit} Sekunden: {resultierende_distanz} Meter")




# from decimal import Decimal, getcontext
# import math
# import multiprocessing


# radius = Decimal('6374340')
# distanz = Decimal('87654321')

# def schwerkraft_stärke(distanz):
#     G = Decimal('6.67430E-11')
#     M1 = (Decimal('9.81') * (radius**2) / G)
#     r = distanz + radius
#     g = G * (M1 / r**2)
#     return g

# def beschleunigung(beschl, schwerkr):
#     v = (beschl**2 + Decimal('2') * schwerkr * Decimal('1')).sqrt()
#     return v

# def berechne_hoehe(zeit):
#     aktuelle_beschl = Decimal('0')
#     aktuelle_dist = Decimal('0')  # Starte bei der Oberfläche der Erde
#     aktuelle_zeit = Decimal('0')
#     getcontext().prec = 28  # Präzision für Dezimalzahlen

#     while aktuelle_zeit < zeit:
#         aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(radius + aktuelle_dist))
#         zeit_schritt = aktuelle_beschl / schwerkraft_stärke(radius + aktuelle_dist)
#         # Multiplikation der Schrittweite mit einem Bruchteil der Sekunde
#         aktuelle_zeit += zeit_schritt * Decimal('0.0000001')  # Ein Tausendstel einer Sekunde
#         aktuelle_dist += Decimal('1')
#         # if aktuelle_dist % 100000 == 0: print(aktuelle_dist)
#         # if aktuelle_zeit % 1 == 0: print(aktuelle_zeit)

#     return aktuelle_dist

# gesuchte_zeit = Decimal('755367.5351298475669')
# hoehe = berechne_hoehe(gesuchte_zeit)
# print(hoehe)

# gesuchte_zeit = Decimal('755367.5351298475669')
# hoehe = berechne_hoehe(gesuchte_zeit)
# print(hoehe)

# from decimal import Decimal, getcontext
# import math

# radius = Decimal('6374340')
# distanz = Decimal('87654321')

# def schwerkraft_stärke(distanz):
#     G = Decimal('6.67430E-11')
#     M1 = (Decimal('9.81') * (radius**2) / G)
#     r = distanz + radius
#     g = G * (M1 / r**2)
#     return g

# def beschleunigung(beschl, schwerkr):
#     v = (beschl**2 + Decimal('2') * schwerkr * Decimal('1')).sqrt()
#     return v

# # def berechne_hoehe(zeit):
# #     aktuelle_beschl = Decimal('0')
# #     aktuelle_dist = Decimal('0')  # Starte bei der Oberfläche der Erde
# #     aktuelle_zeit = Decimal('0')
# #     schrittweite = Decimal('0.0001')  # Starte mit einer größeren Schrittweite
# #     getcontext().prec = 100  # Präzision für Dezimalzahlen

# #     while aktuelle_zeit < zeit:
# #         aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(radius + aktuelle_dist))
# #         zeit_schritt = aktuelle_beschl / schwerkraft_stärke(radius + aktuelle_dist)

# #         # Verkleinere die Schrittweite schrittweise
# #         if aktuelle_zeit + zeit_schritt > (zeit / Decimal('100')):
# #             # Letzter Schritt: Passen die Schrittweite an, um die genaue Zielzeit zu erreichen
# #             zeit_schritt = zeit - aktuelle_zeit
# #             aktuelle_dist += zeit_schritt * schrittweite
# #             aktuelle_zeit = zeit
# #         else:
# #             aktuelle_zeit += zeit_schritt
# #             aktuelle_dist += zeit_schritt * schrittweite
# #             schrittweite /= Decimal('2')  # Halbiere die Schrittweite

# #     return aktuelle_dist

# def berechne_hoehe(zeit):
#     aktuelle_beschl = Decimal('0')
#     aktuelle_dist = Decimal('0')  # Starte bei der Oberfläche der Erde
#     aktuelle_zeit = Decimal('0')
#     getcontext().prec = 28  # Präzision für Dezimalzahlen

#     while aktuelle_zeit < zeit:
#         aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(radius + aktuelle_dist))
#         zeit_schritt = aktuelle_beschl / schwerkraft_stärke(radius + aktuelle_dist)
#         # Verringerung der Schrittweite allmählich mit jedem Schleifendurchlauf
#         aktuelle_zeit += zeit_schritt / (Decimal('2') * aktuelle_dist + Decimal('1'))
#         aktuelle_dist += Decimal('1')

#     return aktuelle_dist

# gesuchte_zeit = Decimal('755367.5351298475669')
# hoehe = berechne_hoehe(gesuchte_zeit)
# print(hoehe)

# # # # # # # from decimal import Decimal, getcontext
# # # # # # # import math

# # # # # # # radius = Decimal('6374340')
# # # # # # # distanz = Decimal('87654321')

# # # # # # # def schwerkraft_stärke(distanz):
# # # # # # #     G = Decimal('6.67430E-11')
# # # # # # #     M1 = (Decimal('9.81') * (radius**2) / G)
# # # # # # #     r = distanz + radius
# # # # # # #     g = G * (M1 / r**2)
# # # # # # #     return g

# # # # # # # def beschleunigung(beschl, schwerkr):
# # # # # # #     v = (beschl**2 + Decimal('2') * schwerkr * Decimal('1')).sqrt()
# # # # # # #     return v

# # # # # # # def berechne_hoehe(zeit):
# # # # # # #     aktuelle_beschl = Decimal('0')
# # # # # # #     aktuelle_dist = Decimal('0')  # Starte bei der Oberfläche der Erde
# # # # # # #     aktuelle_zeit = zeit  # Starte mit der gegebenen Gesamtzeit
# # # # # # #     getcontext().prec = 500  # Präzision für Dezimalzahlen

# # # # # # #     while aktuelle_zeit > 0:
# # # # # # #         # Schritt in Metern für die nächste Berechnung
# # # # # # #         dist_schritt = Decimal('0.01')

# # # # # # #         # Berechne die Zeit, die für diesen einen Meter benötigt wird
# # # # # # #         zeit_schritt = aktuelle_beschl / schwerkraft_stärke(radius + aktuelle_dist)
        
# # # # # # #         # Wenn die verbleibende Zeit nicht ausreicht, um einen weiteren Meter zu berechnen
# # # # # # #         if zeit_schritt > aktuelle_zeit:
# # # # # # #             dist_schritt = aktuelle_zeit * schwerkraft_stärke(radius + aktuelle_dist)
# # # # # # #             aktuelle_zeit = Decimal('0')  # Keine verbleibende Zeit übrig
# # # # # # #         else:
# # # # # # #             aktuelle_zeit -= zeit_schritt  # Ziehe die Zeit für diesen Schritt ab

# # # # # # #         aktuelle_dist += dist_schritt  # Addiere den Schritt zur Gesamtdistanz
# # # # # # #         aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(radius + aktuelle_dist))

# # # # # # #     return aktuelle_dist

# # # # # # # gesuchte_zeit = Decimal('755367.5351298475669')
# # # # # # # hoehe = berechne_hoehe(gesuchte_zeit)
# # # # # # # print(f"Das Objekt war {hoehe} Meter über der Erde zur Zeit {gesuchte_zeit} Sekunden.")



# if __name__ == "__main__":
#     gesuchte_zeit = Decimal('755367.5351298475669')
#     num_processes = 24  # Anzahl der Prozesse
#     pool = multiprocessing.Pool(processes=num_processes)

#     chunk_size = gesuchte_zeit // num_processes

#     results = pool.starmap(berechne_hoehe, [(i, i + chunk_size) for i in range(0, gesuchte_zeit, chunk_size)])

#     final_height = sum(results)
#     print(final_height)