import random
from turtle import Turtle

COLOURS=["Red","Yellow","Pink","Green","Orange","Purple","Blue"]

class Car:
    def __init__(self) -> None:
        self.list_of_cars=[]

    def create_car(self):
        """
        Create a car object and add it to the list of cars.
        The location should be randomised to a certain extent but allow enough space between cars for a frog to pass
        """
        new_car=Turtle(shape="square")
        new_car.shapesize(stretch_len=3)
        new_car.color(random.choice(COLOURS))
        new_car.penup()


        xlocation=random.randint(300, 600)
        ylocation=random.randrange(-240, 260, 100)
        # TODO: At higher speeds this becomes too uniform, improve spacing
        for car in self.list_of_cars:
            if ylocation == car.ycor():
                if xlocation - car.xcor() < 150:
                    xlocation = car.xcor() + 150
        new_car.goto(x=xlocation, y=ylocation)
        new_car.setheading(180)

        self.list_of_cars.append(new_car)

    def car_move(self):
        for car in self.list_of_cars:
            car.forward(10)
