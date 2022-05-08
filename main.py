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
}

COINS = {
    'quarters': .25,
    'dimes': .10,
    'nickels': .05,
    'pennies': .01,
}

'''Function that checks the resources dictionary and MENU dictionary:
    - uses for loop to dynamically check all ingredients need and if there's enough resources.
    '''
def sufficient_resources(m_resources, drink_name):
    drink_ingredients = drink_name["ingredients"]
    for item in drink_ingredients:
        single_ingredient = drink_ingredients[item]
        if m_resources[item] >= single_ingredient:
            continue
            
        else:
            print(f"Sorry, not enough {item}")
            return False
    # print('meets requirements')
    return True

'''Function asks for money input and checks if amount is enough:
    - For loop that taps into coin dictionary and asks user's amount input for each coin.
    - Multiplies amount by coin dict, then adds amount and tally's it into money_amount variable.
    - Returns money_amount to be used on main program.
    '''
def calculate_coins(coins_ref):
    money_amount = 0
    for coin in coins_ref:
        money_inserted = int(input(f'How many {coin}: '))
        coin_value = coins_ref[coin]
        money_convert = coin_value * money_inserted
        print(f"{coin} converted: {round(money_convert, 2)}")
        money_amount += money_convert
        money_amount = float(round(money_amount, 2))
    print(f"\ntotal amount inserted: {money_amount}\n")
    return money_amount       

'''Function that taps into resources dictionary and uses MENU dict to adjust resources:
    - Subtracts resources dictionary and updates the dictionary.
    '''
def make_drink(m_resources, d_ingred):
    drink_ingredients = d_ingred["ingredients"]
    for item in drink_ingredients:
        single_ingredient = drink_ingredients[item]
        m_resources[item] -= single_ingredient

############ MAIN PROGRAM STARTS HERE: ############

is_on = True
bank = 0

while is_on:

    command = input("What would you like? ").lower()

    if command == 'off':
        is_on = False

    elif command == 'report':
        print(resources)
        print(f"Bank: {bank}")

    else:
        if command not in MENU:
            print("Sorry, that's not on the menu or valid command.")
            pass

        else:
            # print(resources)

            # Resources check logic:
            drink_name = command
            # print(drink_name)
            drink = MENU[drink_name]

            is_enough = sufficient_resources(resources, drink)
            # print(is_enough)

            # Money Logic:
            if is_enough:
                # print("keep going")
                total_inserted = calculate_coins(COINS)
                drink_price = drink['cost']
                print(f"the {drink_name}'s price is: {drink_price}\n")
                if total_inserted >= drink_price:
                    change = total_inserted - drink_price
                    bank += drink_price
                    print(f"Your change is: ${change}")
                    
                    # Makes Drink:
                    make_drink(resources, drink)
                    print(f"Here's your {drink_name}\n")
                
                else:
                    print("Not enough money, Please choose another option.")



    
            



