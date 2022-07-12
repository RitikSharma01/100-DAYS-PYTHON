import random
com_choice = random.randint(1, 101)
print(com_choice)


print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :  ")
if choose_difficulty == 'hard':
    total_chances = 5
elif choose_difficulty == 'easy':
    total_chances = 10
else:
    print('Error!!!!!!, Try again')

while total_chances > 0 or com_choice == players_guess:
    print(f"You have {total_chances} attempts remaining to guess the number")
    players_guess = int(input("Make a guess: "))
    if players_guess > com_choice:
        print("Too High")
    elif players_guess < com_choice:
        print("Too low")
    elif total_chances <= 0:
        print("You Loose")
    else:
        print(f"You got it! The answer was {com_choice}")
        total_chances = 0
    total_chances -= 1
    if total_chances == 0:
        print("You've run out of guesses,You Loose")
