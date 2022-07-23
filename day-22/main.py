import time
from turtle import Turtle, Screen, width, xcor
from paddle import Paddle
from ball import Ball
from new_score import Scoreboard
4


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
b_ball = Ball()
scoreboard = Scoreboard()


screen.onkey(fun=r_paddle.upward, key='Up')
screen.onkey(fun=r_paddle.downward, key='Down')
screen.onkey(fun=l_paddle.upward, key='a')
screen.onkey(fun=l_paddle.downward, key='z')


while scoreboard.game_is_on:
    time.sleep(b_ball.sleep_time)
    screen.update()
    b_ball.move()
    # detect colision
    if b_ball.ycor() > 280 or b_ball.ycor() < -280:
        # need to bounce
        b_ball.bounce_y()

    # distance of thepaddle
    if b_ball.distance(r_paddle) < 50 and b_ball.xcor() > 320 or b_ball.distance(l_paddle) < 50 and b_ball.xcor() < -320:
        b_ball.bounce_x()

    if b_ball.xcor() > 360:
        b_ball.reset_position()
        scoreboard.l_point()

    if b_ball.xcor() < -360:
        b_ball.reset_position()
        scoreboard.r_point()

    scoreboard.check_score()


screen.exitonclick()
