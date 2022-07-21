from turtle import Turtle, Screen, width, xcor

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('The Pong Game')
screen.tracer(0)
screen.listen()

tim = Turtle()
tim.shape('square')
tim.color('white')
tim.shapesize(stretch_wid=5, stretch_len=1)
tim.speed(0)
tim.penup()
tim.setpos(350, 0)


def up():
    new_ycor = tim.ycor()+20
    tim.goto(tim.xcor(), new_ycor)


def down():
    new_ycor = tim.ycor()-20
    tim.goto(tim.xcor(), new_ycor)


def stop():
    game_is_on = False


screen.onkey(fun=up, key='Up')
screen.onkey(fun=down, key='Down')
screen.onkey(fun=stop, key='a')


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
