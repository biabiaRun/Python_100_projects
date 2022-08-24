from turtle import Turtle, Screen
import time
from snake import Snake

# TODO: 0-SET UP SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer()


snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right ")


# TODO: 1-CREATE A SNAKE BODY
## Three turtles in square shape lined


# TODO: 2-MOVE THE SNAKE
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()