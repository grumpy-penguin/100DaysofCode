from turtle import Turtle

ALIGNMENT = "center"
FONT = ("console", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=-250, y=250)
        self.scoreboard()

    def scoreboard(self):
        self.write(arg=f"Level { self.level }", move=False, align=ALIGNMENT, font=FONT)

    def nextlevel(self):
        self.level += 1
        self.clear()
        self.scoreboard()

    def gameover(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
