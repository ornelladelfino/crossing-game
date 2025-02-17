from turtle import Screen
import time
from player import Player
from cars import CarMachine
from levels import Levels

screen=Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_dealer = CarMachine()
levels =Levels()

screen.listen()
screen.onkey(player.move, "Up")

game_on= True
while game_on:

    screen.update()
    time.sleep(car_dealer.moving_speed)
    car_dealer.create_car()
    car_dealer.moving_car()

    for car in car_dealer.all_cars:
        if player.distance(car) < 20:
            levels.game_over()
            game_on = False

    if player.ycor() > 290:
        player.reset_player()
        levels.level_up()
        car_dealer.speed_up()




screen.exitonclick()