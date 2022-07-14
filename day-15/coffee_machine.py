

MENU = {
    'espresso': {
        'ingredients': {
            'water': 100,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}


def pay_money():
    print("Please insert coins")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    total_coins_value = 0.25*quarters+0.10*dimes+0.05*nickles+0.01*pennies
    return total_coins_value


def resources_update(coffee):
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    resources['money'] += MENU[coffee]['cost']
    if coffee != 'espresso':
        resources['milk'] -= MENU[coffee]['ingredients']['milk']


def check_resources(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        return False
    else:
        return True


def machine(coffee):
    if check_resources(coffee):
        money_paid = pay_money()
        resources_update(coffee)
        if money_paid >= MENU[coffee]['cost']:
            # return_money = round(money_paid-MENU['latte']['cost'], 2)
            return_money = round(money_paid-MENU[coffee]['cost'], 2)
            print(f"Here is {return_money} in change.")
            print(f"Here is your {coffee} Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry there is not enough water")


is_on = True


while is_on:
    demand = input("What would you like? (espresso/latte/cappuccino): ")

    if demand == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif demand == 'latte' or demand == 'espresso' or demand == 'cappuccino':
        machine(demand)

    elif demand == 'off':
        is_on = False
        # check_resources('latte')
        # money_paid = pay_money()
        # resources_update('latte')
        # if money_paid >= MENU['latte']['cost']:
        #     # return_money = round(money_paid-MENU['latte']['cost'], 2)
        #     return_money = round(money_paid-MENU['latte']['cost'], 2)
        #     print(f"Here is {return_money} in change.")
        #     print("Here is your latte Enjoy!")

    # elif demand == 'espresso':
        # check_resources('espresso')
        # money_paid = pay_money()
        # resources_update('espresso')
        # if money_paid >= MENU['espresso']['cost']:
        #     # return_money = round(money_paid-MENU['latte']['cost'], 2)
        #     return_money = round(money_paid-MENU['espresso']['cost'], 2)
        #     print(f"Here is {return_money} in change.")
        #     print("Here is your espresso Enjoy!")
    # elif demand == 'cappucccino':
        # check_resources('cappuccino')
        # money_paid = pay_money()
        # resources_update('cappucccino')
        # if money_paid >= MENU['cappucccino']['cost']:
        #     # return_money = round(money_paid-MENU['latte']['cost'], 2)
        #     return_money = round(money_paid-MENU['cappucccino']['cost'], 2)
        #     print(f"Here is {return_money} in change.")
        #     print("Here is your cappucccino Enjoy!")
