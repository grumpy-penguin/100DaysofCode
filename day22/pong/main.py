from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_over = False
player_left = Paddle(location=-350)
player_left_score = Scoreboard(xcor=-150)
player_right_score = Scoreboard(xcor=150)
player_right = Paddle(location=350)
ball = Ball()

screen.listen()
screen.onkey(fun=player_left.moveup, key="w")
screen.onkey(fun=player_left.movedown, key="s")
screen.onkey(fun=player_right.moveup, key="Up")
screen.onkey(fun=player_right.movedown, key="Down")

# ball.move_ball()
game_count = 0
game_speed = 0.09

while not game_over:

    screen.update()
    sleep(ball.game_speed)
    ball.move_ball()

    # Detect collision with roof and floor, then bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(cor="y")

    # Detect collision with player paddle, then bounce
    if (
        ball.distance(player_left) < 50
        and ball.xcor() < -330
        or ball.distance(player_right) < 50
        and ball.xcor() > 330
    ):
        ball.bounce(cor="x")

    # Detect when left player misses the ball
    if ball.xcor() > 380:
        player_left_score.add_score()
        ball.reset_position()

    # Detect whent the right player misses the ball
    if ball.xcor() < -380:
        player_right_score.add_score()
        ball.reset_position()

    if player_right_score.score == 10 or player_left_score.score == 10:
        game_count += 1

screen.exitonclick()
