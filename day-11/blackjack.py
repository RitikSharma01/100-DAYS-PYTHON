import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
is_game_over = False
for i in range(0, 2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_score = calculate_score(player_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards :{player_cards}")
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
