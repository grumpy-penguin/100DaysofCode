from turtle import Turtle

START_XLOCATION = 0
START_YLOCATION = -280


class Frog(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(x=START_XLOCATION, y=START_YLOCATION)
        self.gamespeed = 0.1

    def move(self):
        self.forward(20)

    def reset(self):
        self.goto(x=START_XLOCATION, y=START_YLOCATION)
        self.gamespeed *= 0.5
