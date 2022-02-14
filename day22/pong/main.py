# There are two players

# Each player has a bats
# Each bat can respond up or down to the users key press
# Each player has a score

# A ball travels between the two bats
# If a ball hits a bat it returns at a random angle
# If a ball misses a bat the opposite players score is increased

# The score is kept at the top of the play area
# The score increases when a player returns the ball and the opponent misses
# The game ends when a player reaches a score of 5

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
ball=Ball()

screen.listen()
screen.onkey(fun=player_left.moveup, key="w")
screen.onkey(fun=player_left.movedown, key="s")
screen.onkey(fun=player_right.moveup, key="Up")
screen.onkey(fun=player_right.movedown, key="Down")

# ball.move_ball()

while not game_over:
    screen.update()
    sleep(0.05)
    ball.move_ball()

    # Detect collision with roof and floor, then bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(cor="y")

    # Detect collision with player paddle, then bounce
    if ball.distance(player_left) < 50 and ball.xcor() < -330 or ball.distance(player_right) < 50 and ball.xcor() > 330:
        ball.bounce(cor="x")

    # Detect when left player misses the ball
    if ball.xcor() > 380:
        ball.ball_speed()
        player_left_score.add_score()
        ball.reset_position()

    # Detect whent the right player misses the ball
    if ball.xcor() < -380:
        ball.ball_speed()
        player_right_score.add_score()
        ball.reset_position()


screen.exitonclick()
