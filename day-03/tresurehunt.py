print('Welcome to the Tresure Island.')
print('Your mission is to find Tresure.')
direction = input(
    "You are in cross roads, Where do you wants to go 'left' or 'right' \n")
if direction == 'left':
    waterways = input(
        'You come to a lake. There is a Island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim accross \n')
    if waterways == 'wait':
        door = input(
            'You arrive to the island unharmed.There are three doors red , blue ,yellow.Which one to choose \n')
        if door == 'yellow':
            print("You Win the game")
        else:
            print('Game over.There was a lion behind the door')
    else:
        print('Game Over.The lake was full of crocodiles.')
else:
    print('Game Over. You choose the wrong direction')
