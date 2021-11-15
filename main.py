from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
is_on = True

while is_on:
    # uses get_items() method to print menu items
    choice = input(f"What would you like? {my_menu.get_items()} :")
    drink = my_menu.find_drink(choice)
    # print(coffee_maker.resources["water"])
    # print(menu)
    # print(my_menu.find_drink(choice).ingredients)
    # print(menu.find_drink(choice).name)
    if choice == "off":
        # exactly the same as the original script
        is_on = False
    elif choice == "report":
        # this calls the report function in the coffee_maker class
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        # specify drink in menu class with find_drink method
        if my_coffee_maker.is_resource_sufficient(drink):
            # if resources sufficient this is true.
            # print("hello")
            if my_money_machine.make_payment(drink.cost):
                # print("make payment")
                my_coffee_maker.make_coffee(drink)
