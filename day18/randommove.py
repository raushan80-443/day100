# import turtle
import random
# turtle.colormode(255)
# screen = turtle.Screen()
# raj = turtle.Turtle()
# raj.pensize(20)
# raj.speed(0)


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ranomcol = (r, g, b)
    return ranomcol


# direction = [0, 90, 180, 270]
# for a in range(500):
#     raj.fd(30)
#     raj.setheading(random.choice(direction))
#     raj.color(randomcolor())
#
# screen.exitonclick()
