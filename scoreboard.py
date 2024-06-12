FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    level = 1

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220,220)
        self.write(f"Level {self.level}",font=FONT)

    def nextLevel(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", font=FONT)

    def gameOver(self):
        self.clear()
        self.goto(-150,0)
        self.write(f"GAME OVER! Last Level: {self.level}", font=FONT)

