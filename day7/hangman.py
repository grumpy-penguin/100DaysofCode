import random
from os import system
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guess_history = []
end_of_game = False
lives = 6

print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    system("clear")
    if guess not in guess_history:
        guess_history.append(guess)
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You chose {guess}, this isn't in the word. You've been hung.")
            else:
                print(f"You chose {guess}, this isn't in the word. Try again.")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
    else:
        print(f'You\'ve already used "{guess}", please choose another letter.')
    print(stages[lives])
