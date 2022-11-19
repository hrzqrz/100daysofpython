from importlib import resources


MENU = {
    'espersso':{
        'ingredients':{
            'watter': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte':{
        'ingredients':{
            'watter': 200,
            'milk':150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino':{
        'ingredients':{
            'watter': 250,
            'milk':100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}
resurces = {
    'watter' : 300,
    'milk' : 200,
    'coffee' : 100
}

profit = 0

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resurces[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resurces[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins.')
    total = int(input('how many quarters?: ')) * 0.25
    total += int(input('how many dimes?: ')) * 0.1
    total += int(input('how many nickles?: ')) * 0.05
    total += int(input('how many pennies?: ')) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or False if money is dinsufficient."""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. money refunded.")
        return False

is_on = True
while is_on:
    choice = input('What would you like? (espresoo/latte/cappuccino)')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Watter: {resurces['watter']} ml")
        print(f"Milk: {resurces['milk']} ml")
        print(f"Coffee: {resurces['coffee']} g")
        print(f"Money: $ {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
        # print(drink)