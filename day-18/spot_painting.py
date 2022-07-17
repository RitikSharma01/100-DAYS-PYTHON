import turtle
import random
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed(0)
# timmy.setpos(-300, -250)
a = 30
for i in range(10):
    b = -250 + 50*(i)
    timmy.setpos(-300, b)
    for i in range(10):
        timmy.color(random_color())
        timmy.dot(35)
        timmy.forward(70)


screen = turtle.Screen()
screen.exitonclick()
