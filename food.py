from turtle import Turtle
from random import randint

SQUARE_UNITS = 260

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=15/20, stretch_wid=15/20)
        self.color("aquamarine")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(-SQUARE_UNITS, SQUARE_UNITS), randint(-SQUARE_UNITS, SQUARE_UNITS))
