import random
from art import logo

SECRET_NUMBER = random.randint(1, 100)
HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


def choose_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard':") == "hard":
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS


def compare_number(secret_number, guess, attempts):
    """Check the guess against the secret number. Returns the number of remaining attemtps."""
    if guess == SECRET_NUMBER:
        print(f"You got it! The answer was {SECRET_NUMBER}")
        return 0
    elif guess > SECRET_NUMBER:
        print("To High\nGuess Again")
        if attempts == 1:
            print(
                f"You've run out of guesses, you lose. The number I was thining of is {secret_number}."
            )
        return attempts - 1
    else:
        print("Too low\nGuess again.")
        if attempts == 1:
            print(
                f"You've run out of guesses, you lose. The number I was thining of is {secret_number}."
            )
        return attempts - 1


def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100. Try and guess it.")

    attempt = choose_difficulty()
    while attempt > 0:
        print(f"You have { attempt } attempts remaining to guess the number.")
        users_guess = int(input("Make a guess: "))

        attempt = compare_number(SECRET_NUMBER, users_guess, attempt)


game()
