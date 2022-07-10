import random
import art


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Loss, opponent has Blackjack "
    elif user_score > 21:
        return "You went over , Your Loss"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif computer_score > 21:
        return "Opponent went over, You Win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you loose"


def play_game():
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(0, 2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    while not is_game_over:

        user_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards :{player_cards} your score:{user_score}")
        print(f"Computer's cards :{player_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_say = input(
                "Type 'y' to get another card or 'n' to pass: ")
            if user_should_say == 'y':
                player_cards.append(random.choice(cards))
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)
    print(f"Your final Card: {player_cards} , final score={user_score}")
    print(
        f"Computer's final Card: {computer_cards}, final score={computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
