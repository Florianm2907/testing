from decimal import Decimal as d, getcontext
import math

gesuchte_zeit = d('755367.5351298475669')
radius = d('6374340')
distanz = d('87654321')

def schwerkraft_stärke(distanz):
    G = d('6.67430E-11')
    M1 = (d('9.81') * (radius**2) / G)
    r = distanz + radius
    g = G * (M1 / r**2)
    return g

def beschleunigung(beschl, schwerkr):
    v = (beschl**2 + d('2') * schwerkr * d('1')).sqrt()
    return v

def berechne_höhe(zeit):
    aktuelle_beschl = d('0')
    aktuelle_dist = d('0')
    aktuelle_zeit = zeit
    aktuelle_schrittweite = d('0.1')
    getcontext().prec = 100
    
    return