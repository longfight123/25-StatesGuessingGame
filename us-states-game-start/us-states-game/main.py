"""

This script simulates a State guessing game. Try to
guess the names of all 50 states.

This script requires that 'turtle' and 'pandas' be installed within the Python
environment you are running this script in.

"""

import turtle
from question import Question

screen = turtle.Screen()
screen.title('U.S. States Game')
image = './blank_states_img.gif'
screen.addshape(image)
background = turtle.Turtle()
background.shape(image)
game_is_on = True
question = Question()
answer = screen.textinput(title='Guess the State', prompt='What\'s another state\'s name?')

while game_is_on:
    question.check_answer(answer)
    answer = screen.textinput(title=f'Correct States {len(question.correct_states_names)}/50', prompt='What\s another state\'s name?')
    if len(question.correct_states_names) == 50:
        game_is_on = False
    if answer.title() == 'Stop':
        question.generate_missing_states()
        game_is_on = False

screen.exitonclick()
