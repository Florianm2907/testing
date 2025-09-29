# from math import *
# import time as ti

# grav = 9.81
# radius = 6374340
# distance = 87654321
# initial_vel = 0
# g = 6.67430e-11
# m = 5.972e24


# def calculate_time_from_distance(distance, gravitation, initial_vel):
#     time = (-initial_vel+sqrt(initial_vel*initial_vel+2*gravitation*distance))/gravitation
#     return time
    
# def calculate_distance_from_time(time, initial_vel, gravitation):
#     distance = initial_vel*time+0.5*gravitation*(time*time)
#     return distance

# #def calculate_gravity_at_distance(distance, standard_grav):
# #    gravity = standard_grav/(1+(distance/radius)**2)
# #    return gravity

# def calculate_velocity(grav, distance):
#     vel = sqrt(2*grav*distance)
#     return vel
    
# def calculate_gravity_at_distance(distance, standard_grav):
#     gravi =    (g*m)/((radius+distance)**2)
#     return gravi

# #print(calculate_time_from_distance(100, grav, 0))
# #print(calculate_distance_from_time(calculate_time_from_distance(100, grav, 0), 0, grav))
# print(calculate_gravity_at_distance(10000, grav))
# tim = 0
# vel = 0
# print(g)
# print(m)
# for i in range(distance):
#     gravit = calculate_gravity_at_distance((distance-i), grav)
#     t =    calculate_time_from_distance(1, gravit, vel)
#     vel = calculate_velocity(gravit, 1)
#     tim+=t
#     if i%1000000==0:
#         print(tim)     
#         print(vel)
#         print(t)
#         print(i)
#     #ti.sleep(0.02)
# print(tim)
import math
import time as t
import scipy.optimize as opt

radius = 6374340
distanz = 87654321
zeit = 755367.5351298475669
G = 6.67430 * 10**(-11)
M1 = (9.81*(6374340**2)/G)

def schwerkraft_stärke(distanz):
    r = distanz + radius
    g = G * (M1 / r**2)
    return g

def beschleunigung(beschl, schwerkr):
    v = math.sqrt(beschl**2 + 2 * schwerkr * 0.1)
    return v

def equation(x):
    return (x * 343.51 / 4.905)**0.5 - 6.733 + x

def berechne_zeit(distanz):
    aktuelle_beschl = 0
    aktuelle_dist = distanz
    zeit = 0
    for t in range(distanz * 10):
        t /= 10
        zeit_schritt = (beschleunigung(aktuelle_beschl, schwerkraft_stärke(aktuelle_dist)) - aktuelle_beschl) / schwerkraft_stärke(aktuelle_dist)
        zeit += zeit_schritt
        aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(aktuelle_dist)) #- aktuelle_beschl / schwerkraft_stärke(aktuelle_dist)
        aktuelle_dist -= 0.1
        if t % 100000 == 0:
            print(aktuelle_dist)
            print(aktuelle_beschl)
            print(zeit)
        t *= 10
    print(f"Zeit: {zeit}")

def zeit_sch(aktuelle_beschl, aktuelle_dist):
    r = aktuelle_dist + radius
    g = G * (M1 / r**2)
    v = math.sqrt(aktuelle_beschl**2 + 2 * g * 0.1)
    return (v - aktuelle_beschl) / g

def berechne_zeit(distanz):
    aktuelle_beschl = 0
    aktuelle_dist = distanz
    zeit = 0
    for t in range(distanz * 10):
        t /= 10
        zeit_schritt = zeit_sch(aktuelle_beschl, aktuelle_dist)
        # zeit_schritt = (math.sqrt(((aktuelle_beschl**2 + 2 * (G * (M1 / (aktuelle_dist + radius)**2))) * 0.1) - aktuelle_beschl)) / (G * (M1 / (aktuelle_dist + radius)**2))
        zeit += zeit_schritt
        aktuelle_beschl = beschleunigung(aktuelle_beschl, schwerkraft_stärke(aktuelle_dist)) #- aktuelle_beschl / schwerkraft_stärke(aktuelle_dist)
        aktuelle_dist -= 0.1
        if t % 100000 == 0:
            print(aktuelle_dist)
            print(aktuelle_beschl)
            print(zeit)
        t *= 10
    print(f"Zeit: {zeit}")

def berechne_distanz(zeit):
    aktuelle_dist = 0
    aktuelle_beschl = 0
    aktuelle_schw = schwerkraft_stärke(0)
    for i in range(int(zeit * 10000000000000)):
        aktuelle_schw = schwerkraft_stärke(aktuelle_dist)
        

        return
        

print(berechne_distanz(zeit))
# print(berechne_zeit(distanz))
