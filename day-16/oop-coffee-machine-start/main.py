from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_game_on = True
while is_game_on:
    order = menu.get_items()
    choice = input(f"What would you like? ({order}): ").lower()
    if choice == 'report':
        CoffeeMaker().report()
        MoneyMachine().report()
    elif choice == 'off':
        is_game_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
