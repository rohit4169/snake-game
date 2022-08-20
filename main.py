from turtle import Screen
from snake import Snake
from food import Food
from score import scoreboard
import time
# creating screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# moving snake

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
    # detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment)< 10:
            is_game_on = False
            scoreboard.game_over()


            
    #if we had collision with tail :
    #trigger game over
screen.exitonclick()


