logo = '''
 _____        __  __           ___  ___           _     _             
/  __ \      / _|/ _|          |  \/  |          | |   (_)            
| /  \/ ___ | |_| |_ ___  ___  | .  . | __ _  ___| |__  _ _ __   ___  
| |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \ 
| \__/\ (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/ 
 \____/\___/|_| |_| \___|\___| \_|  |_/\__,_|\___|_| |_|_|_| |_|\___|                                                             
'''

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
    "water": 1500,
    "milk": 1000,
    "coffee": 500,
}

profit = 0

print(logo)

def resource_count(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def coins():
    """Returns the total calculated from coins inserted."""
    print("\nPlease insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def transaction_success(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("\nSorry that's not enough money. Money refunded.\n")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!\n")

is_on = True
while is_on:
    choice = input("Would you like an espresso ($1.50), latte ($2.50), or cappuccino ($3.00)? Type 'off' to exit: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}\n")
    else:
        drink = MENU[choice]
        if resource_count(drink["ingredients"]):
            payment = coins()
            if transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
