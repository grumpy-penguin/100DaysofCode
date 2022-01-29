from secrets import choice
from turtle import Turtle
import random

FOOD_COLOR = ["red", "yellow", "pink", "green", "orange", "purple", "blue"]


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(FOOD_COLOR))
        self.speed("fastest")
        self.goto(x=random.randint(-260, 260), y=random.randint(-260, 260))
        self.refresh()

    def refresh(self):
        self.color(random.choice(FOOD_COLOR))
        self.goto(x=random.randint(-260, 260), y=random.randint(-260, 260))
