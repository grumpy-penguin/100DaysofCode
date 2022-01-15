import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def resource_report():
    """Returns a report of available resources"""
    print(f"Water: { resources['water']}ml")
    print(f"Milk: {resources['milk'] }ml")
    print(f"Coffee: { resources['coffee'] }g")
    print(f"Money: ${ resources['money']}")


def check_resources(product):
    for ingredient in MENU[product]["ingredients"]:
        if resources[ingredient] < MENU[product]["ingredients"][ingredient]:
            print(f"Sorry there is not enough { ingredient }")
            return False
        else:
            return True


def check_payment(amount, menu_item):
    """Given the amount of coins inserted and a product. If sufficient """
    if amount < MENU[menu_item]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif amount > MENU[menu_item]["cost"]:
        change = amount - MENU[menu_item]["cost"]
        print(f"Here is { format(change,'.2f') } dollars in change ")
        resources["money"] += MENU[menu_item]["cost"]
        return True
    else:
        resources["money"] += MENU[menu_item]["cost"]
        return True


def process_coins(num_quarters, num_dimes, num_nickels, num_pennies):
    """Takes the number of each denomiation of coin and multiplies it by the value. Returns a sum of all coins that were inserted"""
    val_quarters = num_quarters * 0.25
    val_dimes = num_dimes * 0.10
    val_nickels = num_nickels * 0.05
    val_pennies = num_pennies * 0.01
    return val_quarters + val_dimes + val_nickels + val_pennies


def make_coffe(drink):
    for resource in MENU[drink]["ingredients"]:
        resources[resource] -= int(MENU[drink]["ingredients"][resource])
    print(f"Here is your { drink }. Enjoy! 🍵")


def screen_clear():
    import os

    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")


# TODO: 1. Prompt the user for coffee choice
# TODO: 2. Turn off the coffe machine using key word "off"
# TODO: 3. Print a report of current resources
# TODO: 4. Check availble resources are sufficent to fullfil order
# TODO: 5. Proces coins that have been inserted
# TODO: 6. Check that transaction is succesful
# TODO: 7: Make coffee


def coffee_machine():
    screen_clear()
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        quit()
    elif order == "report":
        resource_report()
    else:
        print("Please insert coins")
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))
        total_coins = process_coins(quarters, dimes, nickels, pennies)
        if check_resources(order):
            if check_payment(total_coins, order):
                make_coffe(order)
    time.sleep(10)
    coffee_machine()


coffee_machine()
