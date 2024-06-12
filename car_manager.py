COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20
from turtle import Turtle
import random
class CarManager(Turtle):
    randomID = random.randint(1,100000)
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.goto(280,random.choice(range(260,-260,-20)))

    def move(self):
        self.goto(self.xcor() - 10, self.ycor())
        if self.xcor() < -300:
            self.clear()

    def checkPlayerHit(self,player = Turtle):
        if self.distance(player.pos()) < 20:
            print("CAR HIT! You dead!")
            return True
        return False

