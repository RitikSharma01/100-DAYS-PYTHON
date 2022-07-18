import random
from turtle import Turtle, Screen
import turtle

red = Turtle()
green = Turtle()
screen = Screen()
screen.setup(500, 400)
screen.listen()

red.color('red')
red.shape("turtle")
green.color("green")
green.shape('turtle')


red.penup()
green.penup()


red.setpos(-230, 50)
green.setpos(-230, 0)
red_distance = 0
green_distance = 0
user_choice = screen.textinput(
    title="Make your bet", prompt="Which turtle is your bet")


def race():
    run_red = random.randint(5, 15)
    run_green = random.randint(5, 15)
    red.forward(run_red)
    green.forward(run_green)
    global red_distance, green_distance
    red_distance += run_red
    green_distance += run_green


def forword_move():
    red.forward(10)
    green.forward(10)


red.speed(6)
green.speed(6)

while red_distance <= 460 and green_distance <= 460:
    # for i in range(10):
    # screen.onkey(key='space', fun=race)
    red.speed(3)
    green.speed(3)
    race()


if red_distance > green_distance and user_choice == 'red':
    print("!!!!!!!Red Turtle win , You are Winner!!!!!!")
elif green_distance > red_distance and user_choice == 'green':
    print("!!!!!!!Green Turtle win , You are Winner!!!!!!")

else:
    print(f"!!!!!! You loose, {user_choice} turtle loose!!!!!!!")


screen.exitonclick()
