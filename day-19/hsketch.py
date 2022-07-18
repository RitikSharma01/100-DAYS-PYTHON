from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()

# timmy
screen.listen()


def move_forward():
    timmy.forward(10)


def move_backword():
    timmy.backward(10)


def turn_colockwise():
    timmy.right(10)


def turn_anticlockwise():
    timmy.left(5)


def clear_all():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


timmy.speed(10)
screen.onkey(key="f", fun=move_forward)
screen.onkey(key='b', fun=move_backword)
screen.onkey(key='c', fun=turn_colockwise)
screen.onkey(key='a', fun=turn_anticlockwise)
screen.onkey(key='space', fun=clear_all)


screen.exitonclick()
