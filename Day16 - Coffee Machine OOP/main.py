logo = '''
 _____        __  __           ___  ___           _     _             
/  __ \      / _|/ _|          |  \/  |          | |   (_)            
| /  \/ ___ | |_| |_ ___  ___  | .  . | __ _  ___| |__  _ _ __   ___  
| |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \ 
| \__/\ (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/ 
 \____/\___/|_| |_| \___|\___| \_|  |_/\__,_|\___|_| |_|_|_| |_|\___|                                                             
'''

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print(logo)

is_on = True
while is_on:
    options = menu.get_items()
    choice = input("Would you like an espresso ($1.50), latte ($2.50), or cappuccino ($3.00)? Type 'off' to exit: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
