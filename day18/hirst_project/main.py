from email.mime import image
from lib2to3.pgen2.tokenize import untokenize
from tracemalloc import DomainFilter
from turtle import Turtle, color, Screen
import turtle
from colorgram import extract
import random

extract = extract('day18\hirst_project\image.jpg', 30)
list_of_colours = []
damien = Turtle()
screen = Screen()
screen.screensize(300,300)

# damien.shape('circle')
damien.penup()
damien.setx(-150.00)
damien.sety(-130.00)
damien.hideturtle()

turtle.colormode(255)

for colour in extract:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    list_of_colours.append((r, g, b))

for _a in range(10):
    for _b in range(10):
        damien.dot(20, random.choice(list_of_colours))
        damien.forward(50)
    damien.sety(damien.ycor() + 50)
    damien.setx(-150.00)


screen.exitonclick()
