import turtle
import randommove

me = turtle.Turtle()
screen = turtle.Screen()
me.turtlesize(10)
me.lt(90)

a = random(random.choices(180,0))
for _ in range(10):
    me.lt(a)
    me.fd(100)

    
screen.exitonclick()
