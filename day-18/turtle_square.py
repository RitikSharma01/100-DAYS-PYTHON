import turtle as t
import random
timmy = t.Turtle()
# Draw square
# i = 1
# while i <= 4:
#     timmy.forward(100)
#     timmy.right(90)
#     i += 1


# Draw a dashed line
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# # draw triangle
# timmy.color("blue")
# for i in range(3):
#     timmy.forward(150)
#     timmy.right(120)

# # draw square
# timmy.color("green")
# for i in range(4):
#     timmy.forward(150)
#     timmy.right(90)

# # draw pentagon
# timmy.color("orange")
# for i in range(5):
#     timmy.forward(150)
#     timmy.right(72)

# # draw hexagon
# timmy.color("pink")
# for i in range(6):
#     timmy.forward(150)
#     timmy.right(60)


# # draw heptagon
# timmy.color("yellow")
# for i in range(7):
#     timmy.forward(150)
#     timmy.right(51.4)


# # draw octagon
# timmy.color("purple")
# for i in range(8):
#     timmy.forward(150)
#     timmy.right(45)


# # draw nonagon
# timmy.color("coral")
# for i in range(9):
#     timmy.forward(150)
#     timmy.right(40)


# # draw decagon
# timmy.color("golden")
# for i in range(10):
#     timmy.forward(150)
#     timmy.right(36)

# draw all shapes
# side = 3
# color = ["purple", "red", 'green', 'yellow', 'blue',
#          'orange', "purple", "red", 'green', 'yellow']
# while side <= 10:
#     timmy.color(color[side-3])
#     for i in range(side):
#         timmy.forward(130)
#         timmy.right(360/side)
#     side += 1

# random color
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# draw a random walk

# color = ["purple", "red", 'green', 'yellow', 'blue',
#          'orange', "purple", "red", 'green', 'yellow']


# direction = [0, 90, 180, 270]
# i = 0
# timmy.pensize(15)
# timmy.speed(0)
# while i < 200:
#     timmy.pencolor(random_color())
#     # timmy.pencolor(random.choice(color))
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))
#     i += 1


# draw circle
timmy.speed(0)
for i in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(3.6)


screen = t.Screen()
screen.exitonclick()
