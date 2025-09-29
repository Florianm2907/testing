from math import *
import time as t
import matplotlib.pyplot as plt

def calculate_sound_speed(temp):
    temp_k = temp + 273.15
    speed = sqrt((1.4*287*temp_k)/0.029)
    return speed

def calculate_fall_distance(time, grav):
    dist = 0.5*grav*(time*time)
    return dist

def calculate_total_time(time, delay):
    return time + delay

def calculate_sound_distance(speed, time):
    return speed * time

def calculate_sound_time(speed, dist):
    return dist/speed

total_time = 6.733
grav = 9.81
temp = 20
time = 0
delay = 0
speed = calculate_sound_speed(temp)

# distance = speed * time
# time = total_time - delay

data = []
data1 = []
data2 = []

# print(calculate_fall_distance(1.43, grav))
for i in range(int(total_time)*1000):
    
    if time + delay == total_time: print(time); print(calculate_fall_distance(time)); break

fig, ax = plt.subplots()

# Plot the data as a line graph


# You can add labels and a title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Simple Line Graph')

# Display the graph
plt.show()