import turtle
import random
turtle.setup(width=1200, height=1000)
s = turtle.Screen()
s.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.penup()
st_pts = [(-550, -450), (550, -450), (0, 450), (-200, 100)]
for x in st_pts:
    t.goto(x)
    t.dot(5, "white")
while True:
    cur = st_pts[random.randint(0, 2)]
    t.goto((t.position()[0] - cur[0])/2, (t.position()[1] + cur[1])/2)
    t.dot(5, "white")
