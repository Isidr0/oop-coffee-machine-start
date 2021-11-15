from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
# menu_item = MenuItem()

print(coffee_maker.resources["water"])
print(menu.get_items())
print(menu.find_drink('latte'))

