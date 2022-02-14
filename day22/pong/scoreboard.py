from turtle import Turtle

ALIGNMENT = "center"
FONT = ("console", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self,xcor) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(y=250, x=xcor)
        self.score=0
        self.scoreboard()

    def add_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def scoreboard(self):
        self.write(arg=f"Score { self.score }", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
