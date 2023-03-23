import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

turtle_img = "us-states-game-start/blank_states_img.gif"
screen.addshape(turtle_img)
turtle.shape(turtle_img)
data = pandas.read_csv("us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states)  < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 correct states", prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    elif answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

    elif len(guessed_states) == 50:
        break




screen.exitonclick()

#read txt file
#   for each line in txt file
#       if line is in list
    
#unistall pandas
#pip install pandas
#pip install turtle
#pip install pandas
