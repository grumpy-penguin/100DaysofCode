import turtle
from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=700)

users_bet = screen.textinput(title="Turtle Racing", prompt="Which turtle will win the race, enter a color [red, pink, purple, green]?")
is_race_on = False
all_turles = []

value = 300
color = [
    "red",
    "yellow",
    "pink",
    "green",
    "orange",
    "purple",
    "blue"
]

for a in range(len(color)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.setposition(x=-240, y=value)
    tim.color(color[a])
    value -= 100
    all_turles.append(tim)

if users_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winner = turtle
            is_race_on = False

if users_bet.lower() == winner.fillcolor():
    print(f"Contratulations, you bet on { users_bet } and the { winner.fillcolor() } turle won!")
else:
    print(f"You lost, you bet on { users_bet } but the { winner.fillcolor() } turtle won!!!")

screen.exitonclick()
