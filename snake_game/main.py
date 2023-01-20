from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# Create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake= Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.move_snake_left, "Left")
screen.onkey(snake.move_snake_right, "Right")
screen.onkey(snake.move_snake_up, "Up")
screen.onkey(snake.move_snake_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect collision with wall        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.high_score()
    
    #keep high score
    scoreboard.high_score()











screen.exitonclick()

















    
    


    




















