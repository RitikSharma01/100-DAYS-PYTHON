from turtle import Turtle, Screen, width, xcor
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('The Pong Game')
screen.tracer(0)
screen.listen()

# tim = Turtle()
# tim.shape('square')
# tim.color('white')
# tim.shapesize(stretch_wid=5, stretch_len=1)
# tim.speed(0)
# tim.penup()
# tim.setpos(350, 0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
b_boll = Ball()


screen.onkey(fun=r_paddle.upward, key='Up')
screen.onkey(fun=r_paddle.downward, key='Down')
screen.onkey(fun=l_paddle.upward, key='a')
screen.onkey(fun=l_paddle.downward, key='z')


game_is_on = True

while game_is_on:
    screen.update()
    # b_boll.move()


screen.exitonclick()
