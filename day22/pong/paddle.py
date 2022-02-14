from asyncio import streams
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location) -> None:
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(x=location, y=0)

    def moveup(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def movedown(self):
        new_ycor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_ycor)
