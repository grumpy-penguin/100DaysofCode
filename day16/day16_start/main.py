from msilib.schema import tables
from tkinter import RIGHT
import turtle
# import another_module

# print (another_module.another_variable)

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('purple')
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# my_screen = turtle.Screen()

# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("South",["Watford","London"], align= "c" )
table.add_column("North",["Scotland","Artic"], align= "c" )
table.header_style = "upper"
print(table)
