def coffee_info(water, milk, beans, empty_cups, money):
    print('The coffee machine has:')
    print(water, 'ml of water')
    print(milk, 'ml of milk')
    print(beans, 'g of coffee beans')
    print(empty_cups, 'disposable cups')
    print(f"${money} of money")


def espresso(water, beans, empty_cups, money):
    # while water >= 250 or beans >= 16:
    if water // 250 != 0 and beans // 16 != 0 and empty_cups >= 1:
        print('I have enough resources, making you a coffee!')
        water -= 250
        beans -= 16
        empty_cups -= 1
        money += 4
        return True
    elif water // 250 == 0:
        print('Sorry, not enough water!')
        return False
    elif beans // 16 == 0:
        print('Sorry, not enough coffee beans!')
        return False
    elif empty_cups == 0:
        print('Sorry, not enough disposable cups')
        return False
    return water, beans, empty_cups, money

def latte(water, milk, beans, empty_cups, money):
    # while water >= 350 or milk >= 75 or beans >= 20:
    if water // 350 != 0 and milk // 75 != 0 and beans // 20 != 0 and empty_cups >= 1:
        print('I have enough resources, making you a coffee!')
        water -= 350
        milk -= 75
        beans -= 20
        money += 7
        empty_cups -= 1
        return True
    elif water // 350 == 0:
        print('Sorry, not enough water!')
        return False
    elif milk // 75 == 0:
        print('Sorry, not enough milk!')
        return False
    elif beans // 20 == 0:
        print('Sorry, not enough coffee beans!')
        return False
    elif empty_cups == 0:
        print('Sorry, not enough disposable cups')
        return False
    return water, beans, empty_cups, money


def cappuccino(water, milk, beans, empty_cups, money):
    # while water >= 200 or milk >= 100 or beans >= 12:
    if water // 200 != 0 and milk // 100 != 0 and beans // 12 != 0 and empty_cups >= 1:
        print('I have enough resources, making you a coffee!')
        water -= 200
        milk -= 100
        beans -= 12
        money += 6
        empty_cups -= 1
        return True
    elif water // 200 == 0:
        print('Sorry, not enough water!')
        return False
    elif milk // 100 == 0:
        print('Sorry, not enough milk!')
        return False
    elif beans // 12 == 0:
        print('Sorry, not enough coffee beans!')
        return False
    elif empty_cups == 0:
        print('Sorry, not enough disposable cups')
        return False
    return water, beans, empty_cups, money


water = 400
milk = 540
beans = 120
empty_cups = 9
money = 550
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        answer = input()
        if answer == '1':
            if espresso(water, beans, empty_cups, money):
                water -= 250
                beans -= 16
                empty_cups -= 1
                money += 4
        elif answer == '2':
            if latte(water, milk, beans, empty_cups, money):
                water -= 350
                milk -= 75
                beans -= 20
                money += 7
                empty_cups -= 1
        elif answer == '3':
            if cappuccino(water, milk, beans, empty_cups, money):
                water -= 200
                milk -= 100
                beans -= 12
                money += 6
                empty_cups -= 1
        else:
            continue
    elif action == 'fill':
        water_fill = int(input('Write how many ml of water the coffee machine has:'))
        milk_fill = int(input('Write how many ml of milk the coffee machine has:'))
        beans_fill = int(input('Write how many grams of coffee beans the coffee machine has:'))
        empty_cups_fill = int(input('Write how many disposable cups of coffee you want to add:'))
        water += water_fill
        milk += milk_fill
        beans += beans_fill
        empty_cups += empty_cups_fill
        continue
    elif action == 'take':
        print(f"I gave you ${money}")
        money = 0
        continue
    elif action == 'remaining':
        coffee_info(water, milk, beans, empty_cups, money)
    else:
        break
