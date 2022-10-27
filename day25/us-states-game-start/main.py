# How many states have been guessed correctly
# Prompt use for a guess
# Correct guesses write to the x,y coor
# Incorrect guesses start the loop again
# Read CSV file to get the state information

from multiprocessing.connection import answer_challenge
import turtle
import pandas

image = "blank_states_img.gif"
state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
correct_gueses = []
learn_state = []

def get_mouse_click_coor(x,y):
    print(x,y)

def check_state(state_answer):
    return state_data['state'].eq(state_answer.title()).any()

screen = turtle.Screen()
screen.setup(height=491, width=725)
# screen.screensize(canvwidth=725, canvheight=491)
screen.screensize(canvheight=246, canvwidth=363)
screen.title("U.S. State Game")
screen.addshape(image)

turtle.shape(image)

while len(correct_gueses) < 50:

    # turtle.onscreenclick(get_mouse_click_coor)
    state_answer = screen.textinput(title=f"Guessed states { len(correct_gueses) } / 50", prompt="Enter a state to add it to the map").title()
    if state_answer == "Exit":
        learn_state = [ state for state in all_states if state not in correct_gueses ]
        # for state in all_states:
        #     if state not in correct_gueses:
        #         learn_state.append(state)
        df = pandas.DataFrame(learn_state)
        df.to_csv("state_to_learn.csv")
        break
    # if check_state(state_answer=state_answer):
    if state_answer in all_states:
        correct_gueses.append(state_answer)
        # guessed_state = (state_data.loc[state_data['state'] == state_answer.title(), ['state','x','y']].values[0])
        state_item = state_data[state_data.state == state_answer]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x=int(state_item.x), y=int(state_item.y))
        state_turtle.write(state_item.state.item())
