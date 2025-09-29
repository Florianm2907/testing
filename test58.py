import math
import scipy.optimize as opt

radius = 6374340

def schwerkraft_stärke(distanz):
    G = 6.67430 * 10**(-11)
    M1 = (9.81*(radius**2)/G)
    r = radius
    g = G * (M1 / r**2)
    return g

def beschleunigung(beschl, schwerkr):
    v = math.sqrt(beschl**2 + 2 * schwerkr * 0.1)
    return v

def calculate_height(time_seconds):
    aktuelle_beschl = 0
    aktuelle_dist = 0
    zeit = 0
    while zeit < time_seconds:
        beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(aktuelle_dist))
        zeit_step = (beschl - aktuelle_beschl) / schwerkraft_stärke(aktuelle_dist)
        aktuelle_beschl = beschl
        aktuelle_dist += 0.1
        zeit += zeit_step

    return aktuelle_dist

time_seconds = float(input("Enter time in seconds: "))
height = calculate_height(time_seconds)
print(f"The height at {time_seconds} seconds is {height} meters.")
