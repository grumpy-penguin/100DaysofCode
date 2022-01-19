import random
from time import time
from turtle import Screen, Turtle
from random import choice
import turtle

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orchid")
timmy_the_turtle.pencolor("red")
timmy_the_turtle.pensize(5)
turtle.colormode(255)

# for _ in range(4):
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
#
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(200)
# timmy_the_turtle.pendown()
#
# for _ in range(3):
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(120)
#
# timmy_the_turtle.penup()
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.pendown()

# for _ in range(15):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
# colours = [
    # "CornflowerBlue",
    # "DarkOrchid",
    # "IndianRed",
    # "DeepSkyBlue",
    # "LightSeaGreen",
    # "wheat",
    # "SlateGray",
    # "SeaGreen",
# ]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return r,g,b
# for _a in range(3, 11):
    # number_of_sides = _a
    # timmy_the_turtle.pencolor(choice(colours))
    # for _ in range(number_of_sides):
        # angle = 360 / number_of_sides
        # timmy_the_turtle.forward(100)
        # timmy_the_turtle.right(angle)

# Random Walk
## Speed up timmy
## Random changes of direciton at each step
## Randon colour each step
# timmy_the_turtle.speed(10)
# number = 0
# while number < 100:
#     tuple_colour = random_colour()
#     type(tuple_colour)
#     timmy_the_turtle.pencolor(tuple_colour)
#     directions = [0, 90, 180, 270]
#     timmy_the_turtle.setheading(choice(directions))
#     timmy_the_turtle.forward(10)
#     number += 1


# Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(round(360 / size_of_gap)):
        timmy_the_turtle.speed('fastest')
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
        timmy_the_turtle.pencolor(random_colour())

draw_spirograph(10)

screen.exitonclick()
