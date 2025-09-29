from turtle import *

bgcolor('black')
# hideturtle()
speed(100000)
for i in range(500):
    if i % 2 == 0:
        color('cyan')
    else:
        color('magenta')
    forward(i * 3)
    left(91)
done()