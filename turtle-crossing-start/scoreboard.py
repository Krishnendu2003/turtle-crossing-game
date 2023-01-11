FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-150,250)
        self.level=0
        self.update_level()


    def increase_level(self):
        self.level+=1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level : {self.level}",align="center",font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


