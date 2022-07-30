
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "usimage.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')
state_name = data['state'].to_list()
xcor_pos = data['x'].to_list()
ycor_pos = data['y'].to_list()


def get_pos_state(state):
    return state_name.index(state)


def goto_pos_state(state):
    pos = get_pos_state(state)
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(x=xcor_pos[pos], y=ycor_pos[pos])
    state_turtle.write(f'{state_name[pos]}', font=("Courier", 8, "normal"))


guessed_state = []
while len(guessed_state) <= 50:
    answer_state = screen.textinput(
        title=f'Guess the State {len(guessed_state)}/50', prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    elif answer_state in state_name:
        goto_pos_state(answer_state)


def show_all_state():
    for i in state_name:
        if i not in guessed_state:
            goto_pos_state(i)


show_all_state()
# print(answer_state)
screen.exitonclick()
