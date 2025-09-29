import random
from turtle import *

hideturtle()
triang = [ "-400,-400", "400,-400", "0,300" ]
dots = [ "10,20" ]

speed(0)
up()
bgcolor('black')
color('cyan')
for dotss in triang:
    x, y = dotss.split(",")
    goto(int(x), int(y))
    dot(10)

def mitte(pos1, pos2):
    x1, y1 = pos1.split(",")
    x2, y2 = pos2.split(",")
    mittex = (float(x1) + float(x2)) / 2
    mittey = (float(y1) + float(y2)) / 2
    return str(mittex) + "," + str(mittey)

while True:
    currdot = random.randint(0, len(triang)-1)
    mittelpunkt = mitte(dots[len(dots)-1], triang[currdot])
    goto(float(mittelpunkt.split(',')[0]), float(mittelpunkt.split(',')[1]))
    dot(3)
    dots.append(mittelpunkt)