from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


coffee_maker.is_resource_sufficient('latte')
print(menu)
name = input(f"What would you like? {menu.get_items()}: ")
print(menu.find_drink(name))




# menu_item.cost = 0
#
# coffee = 0

# choice = input(f"What would you like? {menu.get_items()}: ")
#
#
# menu.find_drink(choice)