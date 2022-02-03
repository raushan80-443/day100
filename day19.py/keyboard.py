import turtle

sachin = turtle.Turtle()
screen = turtle.Screen()


def forward():
    sachin.fd(50)


def backward():
    sachin.backward(50)


def right():
    sachin.right(90)


def left():
    sachin.left(90)


screen.listen()

screen.onkey(forward , "w")
screen.onkey(backward, "s")
screen.onkey(right, "a")
screen.onkey(left, "d")



screen.exitonclick()