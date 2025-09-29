from turtle import *

bgcolor('black')
# hideturtle()
speed(10)
for a in range(500):
    for i in range(10):
        if i % 2 == 0:
            color('cyan')
        else:
            color('magenta')
        forward(i * 3)
        left(90)
        forward(5)
        left(90)
        forward(i * 3)
        right(90)
        forward(5)
        right(90)
    left(90)
done()