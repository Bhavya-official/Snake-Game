from turtle import Screen
import time
from food import *
from snake import *
from scoreboard import *

screen = Screen()
screen.title("Snake Game")
screen.bgcolor('black')

# screen did not change automatically
screen.tracer(0)
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()
is_game_on = True

# add event listener
screen.listen()
screen.onkey(snake.upward, "Up")
screen.onkey(snake.downward, "Down")
screen.onkey(snake.leftward, "Left")
screen.onkey(snake.rightward, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    if food.distance(snake.head) < 15:
        # Generate Food
        food.next_food()

        # Eat food
        for segments in snake.squares:
            while segments.position() == food.position():
                food.next_food()
                print(segments.position())

        # Increse Snake length
        snake.extend()
        scoreboard.update_score()

    # Check for snake collide with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    # Check for snake collide with tail
    for segment in snake.squares:
        if segment != snake.head:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                scoreboard.game_over()
done()
