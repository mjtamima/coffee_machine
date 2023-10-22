MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(order_ingredients):
    """Takes order ingredients as input and returns True if there is sufficient ingredients. Otherwise returns False."""
    for ing in order_ingredients:
        if order_ingredients[ing] > resources[ing]:
            print(f"Sorry there is not enough {ing}")
            return False
        return True


def process_coins():
    """Takes user coins as input and returns the total amount in dollars"""
    print("Please insert coins.")
    q = int(input("How many quarters?: ")) * 0.25
    d = int(input("How many dimes?: ")) * 0.1
    n = int(input("How many nickels?: ")) * 0.05
    p = int(input("How many pennies?: ")) * 0.01
    return q + d + n + p


def transaction_successful(given_money, cost):
    """Takes user money and drink cost, returns True if transaction is successful and prints out the change if any."""
    if given_money >= cost:
        change = round(given_money - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Not enough money. Money is refunded.")
        return False



def make_coffee(order, order_ingredients):
    """Takes in the drink name and required ingredients as input, deducts the required amount from resources
    and prints out the order."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order}. Enjoy!")


money = 0
is_on = True
while is_on:
    usr = input("What would you like? (espresso/latte/cappuccino): ")
    if usr == 'off':
        is_on = False
    elif usr == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[usr]
        if resources_sufficient(drink['ingredients']):
            usr_money = process_coins()
            if transaction_successful(usr_money, drink['cost']):
                money += drink['cost']
                make_coffee(usr, drink['ingredients'])
