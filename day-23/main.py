import time
from turtle import Screen, Turtle

from pyrsistent import s
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()

screen.onkey(fun=player.move_forward, key='Up')
screen.onkey(fun=player.move_backward, key='Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.goto(0, -280)
        car_manager.level_up()
        score.level += 1
        score.print_score()
screen.exitonclick()
