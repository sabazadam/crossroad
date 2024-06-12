from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#285078")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
    def go_up(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x,new_y + MOVE_DISTANCE)

    def go_right(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x + MOVE_DISTANCE,new_y)

    def go_left(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x - MOVE_DISTANCE, new_y)

    def go_down(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x , new_y - MOVE_DISTANCE)