import random
from turtle import Screen
from frog import Frog
from car import Car
from scoreboard import Scoreboard
from time import sleep

list_of_cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Frog Crossing")

scoreboard = Scoreboard()
frog = Frog()
car_garage = Car()

screen.listen()
screen.onkeypress(fun=frog.move, key="Up")

gameover = False

while not gameover:
    screen.update()
    sleep(frog.gamespeed)

    # Move each car object in the list of cars.
    car_garage.create_car()

    car_garage.car_move()
    # Detect collision with car
    for car in car_garage.list_of_cars:
        if frog.distance(car) < 20:
            scoreboard.gameover()
            gameover = True

    if frog.ycor() > 280:
        frog.reset()
        scoreboard.nextlevel()

screen.exitonclick()
