# # from math import *

# # g = 0.0399
# # grav = 9.81
# # radius = 6374.34

# # def calculate_gravity_at_altitude(altitude):
# #     curr_grav = grav / (1 + (altitude / radius))
# #     return curr_grav

# # def calculate_time_from_distance(distance, gravity):
# #     time = sqrt(distance / 0.5 * gravity)
# #     return time

# # def calculate_distance_from_time(time, gravity):
# #     distance = 0.5 * gravity * (time * time)
# #     return distance

# # height = 87654321

# # i = 0
# # while i < height:
    
# #     i+=0.0001    

# from scipy import integrate

# def f(x):

#     return

# a = 0
# b = 87654321

# result, error = integrate.quad(f, a, b)
# print("Result:", result)
# print("Error:", error)

import math

def calculate_fall_time_and_current_gravity(height, gravity_sea_level):
    # Constants
    earth_radius = 6374340  # Earth's radius in meters

    # Calculate fall time
    fall_time = math.sqrt((2 * height) / gravity_sea_level)

    # Calculate current gravity
    current_gravity = gravity_sea_level * (1 - (earth_radius / (earth_radius + height)) ** 2)

    return fall_time, current_gravity

# Input values
height = float(input("Enter the height in meters: "))
gravity_sea_level = float(input("Enter the gravity at sea level (in m/s^2): "))

# Calculate fall time and current gravity
fall_time, current_gravity = calculate_fall_time_and_current_gravity(height, gravity_sea_level)

# Output the results
print(f"Fall time: {fall_time} seconds")
print(f"Current gravity at {height} meters: {current_gravity} m/s^2")
