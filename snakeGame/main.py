from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("wheat")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

score.write_scoreboard()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game = True

while game:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #check if snake touches to food
    if snake.head.distance(food) < 12:
        score.score += 1
        score.clear()
        score.write_scoreboard()
        food.new()
        snake.extend()


    #check if snake touches to screen
    if snake.head.xcor() > 288 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -289:
        game = False
        score.game_over()


    #check if snake touches its tail
    for body in snake.bodyparts[1:]:
        if snake.head.distance(body) < 5:
            game = False
            score.game_over()




screen.exitonclick()




