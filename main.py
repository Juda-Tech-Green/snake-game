from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


current_screen = Screen()
current_screen.setup(width=600, height=600)
current_screen.bgcolor("black")
current_screen.title("Uróboros")
current_screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
current_screen.listen()


current_screen.onkey(key='Up', fun= snake.up)
current_screen.onkey(key='Down', fun= snake.down)
current_screen.onkey(key='Left', fun= snake.left)
current_screen.onkey(key='Right', fun= snake.right)


game_is_on = True
while game_is_on:
    current_screen.update()
    time.sleep(0.15)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:

        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

current_screen.exitonclick()