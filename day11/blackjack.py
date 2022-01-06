import random
import os
from art import logo

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")


def gamers_turn():
    if sum(gamers_hand) > 21:
        print(f"Bust, your score is {sum(gamers_hand)}")
    else:
        if input("Type 'y' to be dealt another card, type 'n' to stand: ") == "y":
            hit = True
        else:
            hit = False
        while hit == True:
            gamers_hand.append(deal_card(player="gamer"))
            print(
                f"You've been dealt {gamers_hand} your current score is {sum(gamers_hand)}"
            )
            hit = False
            gamers_turn()


def dealers_turn():
    if sum(dealers_hand) > 21:
        print(f"Dealer is bust, dealers score is {sum(dealers_hand)}")
    else:
        while sum(dealers_hand) < 17:
            dealers_hand.append(deal_card(player="dealer"))
            print(f"Dealers hand is {dealers_hand}, the dealers score is {sum(dealers_hand)}")
            dealers_turn()


def deal_card(
    player,
):
    card = random.choice(deck)
    if card == 11 and player == "gamer":
        acechoice = int(input("You drew an Ace, would you like this to be 11 or 1?: "))
        if acechoice == 1:
            card = 1
    return card


def setup_game():
    if input("Would you like to play BlackJack? Tpe 'y' or 'n': ") == "y":
        gameon = True
        screen_clear()
    else:
        gameon = False
        screen_clear()
        quit()
    return gameon


def blackjack():
    print(logo)
    # Start players hand
    count = 0
    while count < 2:
        gamers_hand.append(deal_card(player="gamer"))
        count += 1

    print(f"You've been dealt {gamers_hand} your current score is {sum(gamers_hand)}")

    # Start dealers hand
    count = 0
    while count < 2:
        dealers_hand.append(deal_card(player="dealer"))
        count += 1

    print(f"Dealers card is {dealers_hand[0]}")

    gamers_turn()
    dealers_turn()

    if sum(gamers_hand) == 21 and len(gamers_hand) == 2:
        print(f"BlackJack, your hand is {gamers_hand} and your score is {sum(gamers_hand)}, that's BlackJack!!!")
    elif (
        sum(gamers_hand) <= 21
        and sum(gamers_hand) > sum(dealers_hand)
        or sum(dealers_hand) > 21
    ):
        print(
            f"Your hand is {gamers_hand}, you scored {sum(gamers_hand)}. The dealers hand is {dealers_hand}, the dealers score is {sum(dealers_hand)}. You win!"
        )
    elif (
        sum(gamers_hand) == sum(dealers_hand)
        and sum(gamers_hand) <= 21
        and sum(dealers_hand) <= 21
    ):
        print(
            f"Your hand is {gamers_hand}, you scored {sum(gamers_hand)}. The dealers hand is {dealers_hand}, the dealers score is {sum(dealers_hand)}. It's a draw!"
        )
    else:
        print(
            f"Your hand is {gamers_hand}, you scored {sum(gamers_hand)}. The dealers hand is {dealers_hand}, the dealers score is {sum(dealers_hand)}. You lost!"
        )


while setup_game():
    #deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    deck = [11,10]
    dealers_hand = []
    gamers_hand = []
    blackjack()
