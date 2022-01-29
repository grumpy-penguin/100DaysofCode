from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_over = False

while not game_over:
    scoreboard.scoreboard()
    screen.update()
    sleep(0.1)
    snake.move_snake(20)

    # Detect collision with tail
    for body in snake.segments[1 : ]:
        if snake.snake_head.distance(body) < 15:
            game_over = True
            scoreboard.game_over()

    # Detect collision with food and grow snake
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.snake_head.xcor() >275 or snake.snake_head.xcor() < -275 or snake.snake_head.ycor() < -275 or snake.snake_head.ycor() > 275:
        game_over = True
        food.clear()
        scoreboard.game_over()


screen.exitonclick()
