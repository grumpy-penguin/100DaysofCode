# def add(*args):
#     number = 0
#     for n in args:
#         number += n
#     print(number)

# add(1,1,1,1)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)

type(calculate)
