from art import logo
import os

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")
    # print out some text


def add(n1, n2):
    """
    Add two values together
    """
    return n1 + n2


def subtract(n1, n2):
    """
    Subtract a value from another
    """
    return n1 - n2


def multiply(n1, n2):
    """
    Multiply two values
    """
    return n1 * n2


def divide(n1, n2):
    """
    Divide two values
    """
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculation(num1, num2, userOperator):
    return operators[userOperator](num1, num2)


# while join_calc:
def calculator():
    print(logo)
    contcalc = True
    num1 = float(input("What's the first number?: "))

    while contcalc:

        for operator in operators:
            print(operator)
        userOperator = input("Please choose an operator from the options above: ")

        num2 = float(input("What's the second number?: "))

        answer = calculation(num1, num2, userOperator)

        print(f"{num1} {userOperator} {num2} = {answer}")

        if (
            input(
                f"Type 'y' if you would like to perform a further calcultion with {answer} or 'n' start a new calculation: "
            )
            == "y"
        ):
            num1 = answer
        else:
            contcalc = False
            calculator()


calculator()
