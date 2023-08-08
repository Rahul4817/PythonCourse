# from turtle import Turtle,Screen
#Method 1. from=>keyword, turtle=>module, import=>keyword, *=>everything //that mean's turtle module take everything
# Method 2. import=>keyword, turtle=>module, as=>keyword, t=>aliases
from turtle import  *
t=Turtle()
def draw_shape(num_sides):
    if num_sides!=0:
        angle=360/num_sides
        for _ in range(num_sides):
            if angle==num_sides:
                t.forward(100)
                t.right(angle)
            else:
                t.right(50)
                t.forward(20)
draw_shape(100)
screen= turtle.Screen()
screen.exitonclick()
