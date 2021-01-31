def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
    elif front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left
    else:
        turn_left()























def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
