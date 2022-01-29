from turtle import onclick, Turtle, Screen
import turtle

screen=Screen()
screen.listen()
timmy = Turtle()

def north():
    timmy.forward(15)

def east():
    timmy.right(5)

def south():
    timmy.backward(5)

def west():
    timmy.left(5)

def cleardrawing():
    timmy.home()
    timmy.clear()

screen.onkeypress(fun=north, key="w")
screen.onkeypress(fun=south, key="s")
screen.onkeypress(fun=east, key="d")
screen.onkeypress(fun=west, key="a")
screen.onkeypress(fun=cleardrawing, key="c")



screen.exitonclick()
