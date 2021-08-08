from turtle import Turtle
import pandas as pd

FONT = ("Arial", 8, "normal")


class Question(Turtle):
    """
    A class used to represent a control the state
    guessing game.

    ...

    Attributes
    ----------
    dataframe: Dataframe
        a pandas dataframe containing the
        name of the state and the x/y coordinates
        on the map
    correct_states_turtles: list
        list that contains the turtle objects
        representing correctly guessing states
    correct_states_names: list
        a list containing the names of the
        correctly guessed states

    Methods
    -------
    check_answer(answer)
        checks the users answers
    add_correct_state(correct_answer)
        create a turtle object to write the
        name of the state on the map and add to
        correct_states_turtles and correct_states_names
    generate_missing_states()
        generates a csv file that contains states
        that were not guessed
    """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.dataframe = pd.read_csv('./50_states.csv')
        self.correct_states_turtles = []
        self.correct_states_names = []

    def check_answer(self, answer):
        """checks the users answers

        Parameters
        ----------
        answer: str
            The users typed answer
        """
        answer = answer.title()
        for state in self.dataframe['state'].to_list():
            if answer == state and state not in self.correct_states_names:
                self.add_correct_state(answer)

    def add_correct_state(self, correct_answer):
        """create a turtle object to write the
        name of the state on the map and add to
        correct_states_turtles and correct_states_names

        Parameters
        ----------
        correct_answer: str
            The users typed answer
        """
        new_state = Turtle()
        new_state.penup()
        new_state.color('black')
        new_state.speed('fastest')
        new_state.hideturtle()
        x_cor = int(self.dataframe[self.dataframe['state'] == correct_answer]['x'])
        y_cor = int(self.dataframe[self.dataframe['state'] == correct_answer]['y'])
        new_state.goto(x=x_cor, y=y_cor)
        new_state.write(arg=correct_answer, align='center', font=FONT)
        self.correct_states_names.append(correct_answer)
        self.correct_states_turtles.append(new_state)

    def generate_missing_states(self):
        """generates a csv file that contains states
        that were not guessed
        """
        missing_state = [state for state in self.dataframe['state'].to_list() if state not in self.correct_states_names]
        # missing_state = []
        # for state in self.dataframe['state'].to_list():
        #     if state not in self.correct_states_names:
        #         missing_state.append(state)
        missing_state_dataframe = pd.DataFrame(data={'state': missing_state})
        missing_state_dataframe.to_csv('missing_state_dataframe.csv')
