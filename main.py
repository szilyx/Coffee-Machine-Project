from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
myMoneyMachine = MoneyMachine()
coffeMachine = CoffeeMaker()
MyMenu = Menu()
coffe = input(f"What coffe would you like {MyMenu.get_items()}?")
turnoff = False

while turnoff == False:
    if coffe.lower() == "off":
        turnoff = True
        break
    elif coffe == "report":
        coffeMachine.report()
    else:
        drink = MyMenu.find_drink(coffe)
        Source = coffeMachine.is_resource_sufficient(drink)
        if Source == True:
            enough = myMoneyMachine.make_payment(drink.cost)
            if enough == True:
                myMoneyMachine.report()
                coffeMachine.make_coffee(drink)
                coffeMachine.report()
    coffe = input("What coffe would you like?")
