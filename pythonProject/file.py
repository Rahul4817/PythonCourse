import turtle
from turtle import *

speed(1500)

bgcolor("green")
color("yellow")

hideturtle()
n=1
p=True
m=1
t=True

for i in range(400):
    circle(m)
    if t:
        m = m - 1
    else:
        m = m + 2
    if m == 0 or m == 10:
        t = not t


    left(1)
    forward(3)

while True:
    circle(n)
    if p:
        n=n-1
    else:
        n=n+1
    if n==0 or n==60:
        p=not p

    left(1)
    forward(3)
turtle.exitonclick()