import os
import random
from game_data import data
from art import vs, logo

score = 0
### The Game
# Get two objects
def get_choice():
    return random.choice(data)


def highest_option(option_a, option_b):
    if int(option_a["follower_count"]) > int(option_b["follower_count"]):
        return "A"
    else:
        return "B"


def compare_answer(answer, highest):
    if answer.upper() == highest.upper():
        return 0
    else:
        return 1


def keep_score(score):
    score += 1
    return score


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")


def print_choices(object_a, object_b):
    print(logo)
    print(
        f"Compare A: { object_a['name' ]}, a { object_a['description'] }, from { object_a['country'] }."
    )
    print(vs)
    print(
        f"Compare B: { object_b['name'] }, a { object_b['description']} from { object_b['country']}."
    )


def game(a_choice, new_score):
    total_score = new_score
    choice_a = a_choice
    choice_b = get_choice()

    while choice_a == choice_b:
        choice_b = random.choice(data)

    screen_clear()
    print_choices(choice_a, choice_b)

    print(f"Your current score is {total_score}")

    user_answer = input("Who has the most followers? A or B: ")

    if compare_answer(user_answer, highest_option(choice_a, choice_b)) == 0:
        total_score = keep_score(total_score)
        print("You're correct")
        print(f"Your score is: {total_score}")
        game(choice_b, total_score)
    else:
        screen_clear()
        print(logo)
        print("That is incorrect, you lose")
        print(f"Your final score is { total_score }")


_a = get_choice()
game(_a, 0)
