import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


def write_state(state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == state]
    t.goto(x=int(state_data.x), y=int(state_data.y))
    t.write(state)


correct_guesses = []
while len(correct_guesses) < 50:
    user_guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Name a state").title()

    if user_guess == "Exit":
        missed_states = [state for state in states_list if state not in correct_guesses]
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    elif user_guess in correct_guesses:
        pass
    elif user_guess in states_list:
        write_state(user_guess)
        correct_guesses.append(user_guess)
