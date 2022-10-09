from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_maker = MoneyMachine()


while True:
    drink = input("What would you like? (espresso/latte/cappuccino)").lower()

    if drink == "report":
        coffee_machine.report()
        money_maker.report()
    elif drink == "off":
        break
    else:
        drink = menu.find_drink(drink)
        if  drink == None:
            continue
        enough_ingred = coffee_machine.is_resource_sufficient(drink)
        if  not enough_ingred:
            continue
        enough_coins = money_maker.make_payment(drink.cost)
        coffee_machine.make_coffee(drink)