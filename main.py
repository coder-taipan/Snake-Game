from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
# To make the animation smooth.
# When tracer is 0, the screen doesn't update until the screen.update() function is invoked.
screen.tracer(0)

# Step 1- Creating the snake

snake = Snake()
food = Food()
score = Scoreboard()
screen.update()

# Step 2- Animating the snake segments on the screen.

game_is_on = True

# Step 3- How to control the snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)  # Stops the screen for 0.1 seconds.
    snake.move()

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
