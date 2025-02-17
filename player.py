from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVING_DISTANCE = 20
FINISH_LINE_Y = 290

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        new_y= self.ycor() + MOVING_DISTANCE
        self.goto(self.xcor(), new_y)
        #can also be forward()

    def reset_player(self):
        self.goto(STARTING_POSITION)