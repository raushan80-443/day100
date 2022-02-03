import random
from randommove import randomcolor
import turtle as t
circle = t.Turtle()
circle.speed(0)
circle.pensize(5)
t.colormode(255)

def spirogaph(gap_size):
    for time in range(int(360/gap_size)):
        circle.color(randomcolor())
        circle.circle(50)
        circle.setheading(circle.heading() + gap_size)


spirogaph(40)
screen = t.Screen()
screen.exitonclick()
