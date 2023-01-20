from resources import MENU, resources

profit = 0

#keep asking user for input until they enter a valid choice or turn off machine or after order is completed unless no resources
def make_coffee(drink_name, order_ingredients):
    """Makes coffee based on user input"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total   


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False





def report():
    """Prints the current resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(order_ingredients):
    """Checks if there are enough resources to make the drink"""
    for item in order_ingredients['ingredients']:
        if order_ingredients['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
is_on = True
while is_on:
    user_choice= input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        report()
    else:
        drink = MENU[user_choice]
        if check_resources(drink):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
                profit += drink["cost"]
