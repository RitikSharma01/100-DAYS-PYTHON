# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()


def turn_right():
    trun_left()
    trun_left()
    trun_left()


def turn_step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# for i in range(1,7):
#     turn_step()

# num_of_hurdle=6
# while num_of_hurdle>0:
#     turn_step()
#     num_of_hurdle -=1

#  //////////////    HUDLE 2          //////////
# while at_goal != True:
#     turn_step()

# //////////////   HUDLE 3            //////////


while at_goal != True:
    if front_is_clear:
        move()
    elif wall_in_front:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

# ////////////////  HUDLE 4      ///////////////////

while at_goals != True:
    if front_clear():
        move()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
        turn_right()

while at_goals != True:

    if wall_on_right and wall_on_front:
        turn_left()
    if right_is-clear():
        turn_right()
    elif wall_on_right():
        move()
