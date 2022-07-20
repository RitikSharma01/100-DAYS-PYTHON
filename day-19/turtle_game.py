import colorsys
from operator import indexOf
import random
from turtle import Turtle, Screen
import turtle


screen = Screen()
screen.listen()

# create all turtle
# red = Turtle()
# orange = Turtle()
# yellow = Turtle()
# green = Turtle()
# blue = Turtle()
# purple = Turtle()


# # color and shape
# red.color('red')
# red.shape("turtle")

# orange.color("orange")
# orange.shape('turtle')

# yellow.color("yellow")
# yellow.shape('turtle')

# green.color("green")
# green.shape('turtle')

# blue.color("blue")
# blue.shape('turtle')

# purple.color("purple")
# purple.shape('turtle')

# red.penup()
# orange.penup()
# yellow.penup()
# green.penup()
# blue.penup()
# purple.penup()

# # set starting position of each
# red.setpos(-230, 150)
# orange.setpos(-230, 100)
# yellow.setpos(-230, 50)
# green.setpos(-230, -100)
# blue.setpos(-230, 0)
# purple.setpos(-230, -50)

# red_distance = 0
# orange_distance = 0
# yellow_distance = 0
# green_distance = 0
# blue_distance = 0
# purple_distance = 0

# betting

# user_choice = screen.textinput(
#     title="Make your bet", prompt="Which turtle is your bet")


# def race():
#     run_red = random.randint(5, 15)
#     run_orange = random.randint(5, 15)
#     run_yellow = random.randint(5, 15)
#     run_green = random.randint(5, 15)
#     run_blue = random.randint(5, 15)
#     run_purple = random.randint(5, 15)

#     red.forward(run_red)
#     orange.forward(run_green)
#     yellow.forward(run_green)
#     green.forward(run_green)
#     blue.forward(run_green)
#     purple.forward(run_green)

#     global red_distance, orange_distance, yellow_distance, green_distance, blue_distance, purple_distance
#     red_distance += run_red
#     orange_distance += run_orange
#     yellow_distance += run_yellow
#     green_distance += run_green
#     blue_distance += run_blue
#     purple_distance += run_purple


# def forword_move():
#     red.forward(10)
#     green.forward(10)


# red.speed(6)
# green.speed(6)

# while red_distance <= 460 and orange_distance <= 460 and yellow_distance <= 460 and green_distance <= 460 and blue_distance <= 460 and purple_distance <= 460:
#     # for i in range(10):
#     # screen.onkey(key='space', fun=race)
#     red.speed(3)
#     orange.speed(3)
#     yellow.speed(3)
#     green.speed(3)
#     blue.speed(3)
#     purple.speed(3)
#     race()


# if red_distance > green_distance and user_choice == 'red':
#     print("!!!!!!!Red Turtle win , You are Winner!!!!!!")
# elif green_distance > red_distance and user_choice == 'green':
#     print("!!!!!!!Green Turtle win , You are Winner!!!!!!")

# else:
#     print(f"!!!!!! You loose, {user_choice} turtle loose!!!!!!!")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
pos = [-150, -100, -50, 0, 50, 100]
all_turtle = []
dis = []


for i in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    dis.append(0)
    new_turtle.setpos(x=-250, y=pos[i])
    all_turtle.append(new_turtle)


def race(i):
    run = random.randint(5, 15)
    all_turtle[i].forward(run)
    dis[i] += run


user_choice = screen.textinput(
    title="Make your bet", prompt="Which turtle is your bet")

while max(dis) < 300:
    for i in range(0, 6):
        race(i)
maximum = max(dis)
index = dis.index(maximum)
if user_choice == colors[index]:
    print(f'you are winner , {colors[index]} wins')
else:
    print(f'sorry {colors[index]} win, your choice {user_choice} loose ')

screen.exitonclick()
