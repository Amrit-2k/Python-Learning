import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")

screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
player = Player()


car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(player.go_up, "Up")

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        

   

screen.exitonclick()

