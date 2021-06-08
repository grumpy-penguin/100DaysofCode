import os
import art

bidder = {}


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")
    # print out some text


def get_bids(bidder_name, bidder_value):
    """
    Creates a dictionary of bids that will be evaluted to determine who made the winning bid.
    """
    bidder[bidder_name] = bidder_value


def calculate_winning_bid():
    """
    Determine which bidder holds the winning bid.
    """
    winning_bid_value = 0
    winning_bidder = ""
    for bid in bidder:
        if bidder[bid] > winning_bid_value:
            winning_bid_value = bidder[bid]
            winning_bidder = bid
    print(art.logo)
    print(f"The winning bidder is {winning_bidder} with a bid of £{winning_bid_value}")


new_bidder = True

while new_bidder:
    print(art.logo)
    bid_name = input("Enter your name?:\n")
    bid_value = int(input("Enter your bid?: £\n"))
    get_bids(bidder_name=bid_name, bidder_value=bid_value)
    next_bidder = input("Add a new bidder?: \n")
    if (
        next_bidder == "Yes"
        or next_bidder == "yes"
        or next_bidder == "Y"
        or next_bidder == "y"
    ):
        new_bidder = True
        screen_clear()
    else:
        new_bidder = False
        screen_clear()
        calculate_winning_bid()
