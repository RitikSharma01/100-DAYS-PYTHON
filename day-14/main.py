from game_data import data
from art import logo, vs
import random

game_on = True
score = 0
player1 = random.choice(data)
# print(player1)


def checking(player1, player2):
    if player1 != player2:
        return
    else:
        player2 = random.choice(data)


while game_on:
    print(logo)
    print(
        f"Compare A: {player1['name']}, {player1['description']}, {player1['country']}")
    print(art.vs)
    player2 = random.choice(data)
    checking(player1, player2)
    print(
        f"Against B:{player2['name']}, {player2['description']}, {player2['country']}")

    winner = input("Who has more follower? Type 'A' or 'B': ")
    if winner == 'A' and player1['follower_count'] > player2['follower_count']:
        score += 1
        print(f"You're right, Current Score: {score}")
        player1 = player2
    elif winner == 'B' and player1['follower_count'] < player2['follower_count']:
        score += 1
        print(f"You're right, Current Score: {score}")
        player1 = player2
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False
