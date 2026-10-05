import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=728, height=493)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
score = 0
all_states = data["state"].to_list()
correct = []
while score <= 50:
    answer = screen.textinput(title=f"{score}/50 Guess the state", prompt="Whats another state's game?").capitalize()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in correct]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn")
        break
    if answer in all_states:
        state_data = data[data.state == answer]
        new_correct = Turtle()
        new_correct.hideturtle()
        new_correct.penup()
        new_correct.goto(int(state_data.x.item()), int(state_data.y.item()))
        new_correct.write(answer)
        correct.append(new_correct)
        score += 1





