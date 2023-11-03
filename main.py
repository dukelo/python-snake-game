from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard(20)

snake = Snake()
food = Food()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

on_going = True
while on_going:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.reflash()
        score = score+1
        scoreboard.increase_score()
        snake.extend_snake()

    if snake.turtles[0].xcor() < -280 or snake.turtles[0].xcor() > 280 or snake.turtles[0].ycor() < -280 or snake.turtles[0].ycor() > 280:
        on_going = False
        scoreboard.game_over()

    # for turtle in snake.turtles:
    #     if turtle == snake.head:
    #         pass
    #     elif snake.head.distance(turtle) < 10:
    #         on_going = False
    #         scoreboard.game_over()

    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            on_going = False
            scoreboard.game_over()

screen.exitonclick()
