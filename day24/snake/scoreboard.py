from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.highscore = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score: { self.score }  High Score: { self.highscore }",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def add_score(self):
        self.score += 1
        self.scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.scoreboard()
