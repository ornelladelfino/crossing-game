from turtle import Turtle
from random import randint

CAR_COLORS = ["yellow", "red", "blue", "green", "orange", "purple"]
STARTING_MOVING_DISTANCE= 5


class CarMachine:
    def __init__(self):
        self.all_cars=[]
        self.moving_speed=.2

    def create_car(self):
        random_creation=randint(1,6)
        if random_creation==1:
            #this is to prevent too many cars to show at same time.
            new_car=Turtle("square")
            new_car.color(CAR_COLORS[randint(0, 5)])
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, randint(-270, 270))
            self.all_cars.append(new_car)

    def moving_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVING_DISTANCE)

    def speed_up(self):
        self.moving_speed *= .9




