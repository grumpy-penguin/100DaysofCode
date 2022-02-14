from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed()
        self.ball_velocity=1

    def move_ball(self):
        self.goto(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def bounce(self,cor):
        if cor == "y":
            self.y_move *= -1
        else:
            self.x_move *= -1

    def ball_speed(self):
        if self.ball_velocity < 10:
            self.ball_velocity += 1
            self.speed(self.ball_velocity)

    def reset_position(self):
        self.home()
        self.bounce(cor="x")
