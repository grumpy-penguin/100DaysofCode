# FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["fake"])
except FileNotFoundError:
    open("a_file.txt", "a")
except KeyError as error_message:
    print(f"Key {error_message} Doesn't Exist")
else:
    print("File already exists")
finally:
    file.close()
    print("File is now closed")
    raise KeyError("This is grumpy-penguin's made up error")

# # KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

# # IndexError
# fruits = ["Apple", "Banana", "Clementine"]
# fruit = fruits[3]

# # TypeError
# text = "abc"
# print(text + 5)
