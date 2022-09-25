import re
from turtle import Turtle, mode

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")
# DATA_PATH = "day24\\snake\\data.txt"
DATA_PATH = ".\\data.txt"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score: { self.score }  High Score: { self.get_highscore() }",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def add_score(self):
        self.score += 1
        self.scoreboard()

    def reset(self):
        if self.score > self.get_highscore():
            self.store_highscore()
        self.score = 0
        self.scoreboard()

    def store_highscore(self):
        with open(DATA_PATH, "w") as file:
            file.write(str(self.score))

    def get_highscore(self):
        with open(DATA_PATH, "r") as file:
            return int(file.read())
