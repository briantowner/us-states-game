import turtle
import pandas

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=525)
screen.bgpic("blank_states_img.gif")
text = turtle.Turtle()
text.penup()
text.ht()


game_is_on = True
correct_states = 0
answer_list = []
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state's name?").title()
    new_df = data[data.state == answer_state]
    if answer_state in state_list and correct_states < 50:
        text.goto(x=int(new_df.x), y=int(new_df.y))
        text.write(answer_state, False, align="center")
        correct_states += 1
        answer_list.append(answer_state)
    elif answer_state == "Exit":
        break
    elif correct_states == 50:
        game_is_on = False
        print(answer_list)

# states_to_learn.csv
for answer in answer_list:
    state_list.remove(answer)
state_frame = pandas.DataFrame(state_list)
state_frame.to_csv('states_to_learn.csv')

turtle.mainloop()


