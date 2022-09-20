UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle


class Snake:
    """
    Reutrns a snake object. Starting with three segements
    Each object has a move class that moves the snake forward and listens onkeypress "a" to turn the snake right and "d" to turn the snake left.
    """

    def __init__(self) -> None:
        self.xcord = 0
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.goto(x=self.xcord, y=0)
            self.xcord -= 20
            snake.speed("fastest")
            self.segments.append(snake)

    def move_snake(self, distance):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.snake_head.forward(distance)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def grow(self):
        """Add a new segment to a snake"""
        snake = Turtle()
        self.segments.append(snake)
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(x=self.snake_head.xcor() + len(self.segments) * 20, y=0)
        self.xcord -= 20
        snake.speed("fastest")

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]
