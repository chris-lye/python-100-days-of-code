from turtle import pen

from pkg_resources import resource_isdir


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
    "money":0
}

def enough_resources(drink):
    enough = True
    ingredient_not_enough = ""
    for ingredient in MENU[drink]["ingredients"].keys():
        if resources[ingredient]  - MENU[drink]["ingredients"][ingredient] < 0:
            enough = False
            ingredient_not_enough = resources[ingredient]
    return enough, ingredient_not_enough
def enough_money(drink, payment):
    cost = MENU[drink]["cost"]
    change = payment - cost
    if change > 0:
        return  True, change
    else:
        return False, change

def consume_resources(drink):
    for ingredient in MENU[drink]["ingredients"].keys():
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

# penny: 0.01, dime:0.10 , nickel:0.05, quarter:0.25
# print report
while True:
    drink = input("What would you like? (espresso/latte/cappuccino)").lower()

    if drink == "report":
        print(resources)
    elif drink == "off":
        break
    elif drink in ["espresso", "latte", "cappuccino"]:
        enough_ingred, missing_resource = enough_resources(drink)
        if  not enough_ingred:
            print(f"Sorry, not enough {missing_resource}")
            continue
        print("Please insert coins.")
        quarters = int(input(f"how many quarters? (0.01): " ))
        dimes =    int(input(f"how many dimes? (0.10): "))
        nickles =   int(input(f"how many nickles? (0.05): " ))
        pennies =  int(input(f"how many pennies? (0.25): " ))

        total_value = quarters * 0.01 + dimes * 0.10 + nickles * 0.05 + pennies * 0.25
        enough_coins, change = enough_money(drink, total_value)
        if not enough_coins:
            print(f"Sorry {total_value} is not enough money. Money refunded.")
            continue
        else:
            resources["money"] += MENU[drink]["cost"]
            if change > 0:
                print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is your {drink}☕, enjoy!")
        consume_resources(drink)

