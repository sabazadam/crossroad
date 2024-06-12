import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
carList = []
def generateCar():
    amount = random.randint(0,8)
    for i in range(amount):
        car_manager = CarManager()
        carList.append(car_manager)
def moveCar():
    for car in carList:
        car.move()

def checkCarHit():
    for car in carList:
        if car.checkPlayerHit(player):
            return True
    return False
scoreboard = Scoreboard()
player = Player()
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.update()
screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_left,"Left")
screen.onkey(player.go_right,"Right")
screen.onkey(player.go_down,"Down")

game_is_on = True
sleepTime = 0.1
turnAmount = 1
while game_is_on:
    moveCar()
    time.sleep(sleepTime)
    screen.update()
    if turnAmount % 10 == 0:
        generateCar()
    turnAmount += 1
    if checkCarHit():
        scoreboard.gameOver()
        break
    if player.ycor() > 290:
        scoreboard.nextLevel()
        player.goto(0,-290)
        sleepTime -= 0.01
screen.exitonclick()