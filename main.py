import turtle
import pandas

screen = turtle.Screen()
screen.title("Us State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guest_state = []


while len(guest_state) < 50:
    answer = turtle.textinput(title=f"{len(guest_state)}/50 state is correct",
                              prompt="Enter the name of state").title()
    if answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guest_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("Remaining_data.csv")

        break
    if answer in all_states:
        guest_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

screen.exitonclick()
