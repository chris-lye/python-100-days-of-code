import turtle
from numpy import True_
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_on = True
states_correct = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)


while game_on and states_correct < 50:
    answer_state = screen.textinput(title=f"Guess the state:{states_correct}/50 ", prompt="What's another state name?").title()
    if answer_state in all_states:
        all_states.remove(answer_state)
        states_correct += 1
        
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    if answer_state.lower() == "exit":
        game_on = False
        states_left = all_states
        new_data = pandas.DataFrame(states_left)
        new_data.to_csv("states_to_learn.csv")

screen.exitonclick()