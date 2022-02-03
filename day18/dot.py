import randommove
import turtle as t
t.colormode(255)
dot = t.Turtle()
dot.up()
def run():
    b = 0
    for a in range(1, 11):
        dot.goto(0, b)
        for _ in range(1,11):
            dot.color(randommove.randomcolor())
            dot.fd(20)
            dot.dot(20)
        b += 20



run()

screen = t.Screen()
screen.exitonclick()
