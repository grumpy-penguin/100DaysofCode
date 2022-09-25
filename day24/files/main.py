with open("day24\\files\\my_file.txt", mode="a+") as file:
    file.write("\nI'm learning 100Days of Code")

    # with open("day24\\files\\my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
