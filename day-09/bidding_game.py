# from replit import clear
# HINT: You can call clear() to clear the output in the console.
import os
from platform import system
import art
print(art.logo)
bidders = {}
continue_loop = True
while continue_loop:
    name = input("Enter your name ")
    amount = int(input("Enter your bid amount $"))
    bidders[name] = amount
    any_one_left = input('Is there someone to bid ?(yes/no)').lower()
    if any_one_left == 'yes':
        continue_loop = True
        os.system('cls')
    elif any_one_left == 'no':
        continue_loop = False

bid = 0
winner = ''
for key in bidders:
    if bidders[key] > bid:
        bid = bidders[key]
        winner = key
print(f"Winner of this bidding is {winner} with a bid of ${bid}")
