from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.up()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        with open('./highscores.txt',mode='r') as file:
            self.high_score = int(file.read())
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, ALIGNMENT, FONT)
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('./highscores.txt',mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()
