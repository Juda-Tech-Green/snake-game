from turtle import Turtle
from random import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEAD_COLOR = 'purple'


def tail_color():
    red = random()
    green = random()
    blue = random()
    return red, green, blue


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.MOVE_DISTANCE = 20

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        print(f'Size snake {len(self.snake)}')
        body = Turtle(shape="square")
        if (len(self.snake)) % 5 == 0 and len(self.snake)!=0:
            body.color(tail_color())
            if len(self.snake)!=0:
                self.upgradeSpeed()
                print('speed upgraded')
        elif 1 <= len(self.snake) <= 5:
            body.color('white')
        elif len(self.snake) == 0:
            body.color(HEAD_COLOR)
        else:
            body.color(self.snake[-1].pencolor())
        body.up()
        body.goto(position)
        self.snake.append(body)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.MOVE_DISTANCE = MOVE_DISTANCE

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def upgradeSpeed(self):
        self.MOVE_DISTANCE += 0.5

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            if (len(self.snake)) == 3:
                self.snake[seg_num].color('white')
            else:
                self.snake[seg_num].color(self.snake[seg_num].pencolor())
            self.snake[seg_num].goto(self.snake[seg_num - 1].xcor(), self.snake[seg_num - 1].ycor())
        self.snake[0].forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
