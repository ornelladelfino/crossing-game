from turtle import Turtle


class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level=1
        self.display_level()

    def display_level(self):
        self.goto(-220, 240)
        self.write(f"Level {self.level}", align='center', font=('Courier', 20, 'normal'))

    def level_up(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center', font=('Courier', 20, 'normal'))

