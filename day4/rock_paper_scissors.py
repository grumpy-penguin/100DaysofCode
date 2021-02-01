import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
)

computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print("You have made an invalid choice, you lose!!!")
else:
    print("You chose:\n")
    print(rps[user_choice])

    print("The Computer chose:\n")
    print(rps[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!!!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!!!")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win!!!")
    elif user_choice == 1 and computer_choice == 2:
        print("You Lose!!!")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win!!!")
    elif user_choice == 0 and computer_choice == 1:
        print("You Lose!!!")
    else:
        print("Its a draw")
