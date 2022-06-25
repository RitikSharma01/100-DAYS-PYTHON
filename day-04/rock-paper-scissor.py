import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

game = [rock, paper, scissors]
choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (choice > 2 or choice < 0):
    print("Invalid choice")
else:
    print("Your choice")
    print(game[choice])
    comchoice = random.randint(0, 2)
    print("Computer choice")
    print(game[comchoice])
    if(choice == comchoice):
        print("Its a Drow")
    elif choice == 0 and comchoice == 2:
        print("You won")
    elif choice == 1 and comchoice == 0:
        print("You won")
    elif choice == 3 and comchoice == 2:
        print("You won")
    else:
        print("You Loose")
