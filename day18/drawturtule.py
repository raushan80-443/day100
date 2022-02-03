import randommove
import turtle
me = turtle.Turtle()

screen = turtle.Screen()

def draw(numofside):
    angle = 360/numofside
    for a in range(numofside):
        me.fd(200)
        me.rt(angle)

color = ["red","green","blue","black","yellow"]


for a in range(3,8):
   
    me.color("red")
    me.pensize(20)
    me.speed(0)
    draw(a)
   
screen.canvheight(1080)
screen.canvwidth(1920)
screen.exitonclick()
    
    
  
