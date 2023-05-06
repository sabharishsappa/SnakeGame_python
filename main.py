from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    if snake.head.distance(food)<15:
        food.refresh()
        scoreBoard.foodCollision()
        snake.extend()
    if snake.head.xcor()>270 or snake.head.ycor()>270 or snake.head.xcor()<-270 or snake.head.ycor()<-270:
        game_on=False
        scoreBoard.gameOver()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on=False
            scoreBoard.gameOver()
    snake.move()
    time.sleep(0.1)
    screen.update()



screen.exitonclick()