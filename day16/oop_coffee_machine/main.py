from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time


def screen_clear():
    import os

    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")


menu = Menu()
coffee_machine = CoffeeMaker()
coin_machine = MoneyMachine()
coffee_machine_on = True

while coffee_machine_on:
    screen_clear()
    order = input(f"What would you like? ({ menu.get_items() }): ")

    if order == "off":
        coffee_machine_on = False
        screen_clear()
    elif order == "report":
        coffee_machine.report()
        time.sleep(20)
        screen_clear()
    else:
        if coffee_machine.is_resource_sufficient(menu.find_drink(order)):
            if coin_machine.make_payment(menu.find_drink(order).cost):
                coffee_machine.make_coffee(menu.find_drink(order))
                time.sleep(20)
        time.sleep(20)
