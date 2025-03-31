from random import randint

friends = {}
default_value = 0
number = int(input('Enter the number of friends joining (including you):'))


def friend_list(default_value):
    if number <= 0:
        print()
        print('No one is joining for the party')
    else:
        print()
        print('Enter the name of every friend (including you), each on a new line:')
        num = 0
        while num != number:
            friend_name = input()
            friends[friend_name] = default_value
            num += 1


def bill_value(friends, total_bill):
    fr_pay = round((total_bill / number), 2)  # the total bill equally among everyone
    friends_pay = {key: fr_pay for (key, value) in
                   friends.items()}
    print(friends_pay)
    return friends_pay


def lucky(friends, number, total_bill):
    list_friends = []
    random_friend = randint(1, number)
    for obj in friends:
        list_friends.append(obj)
    new_number = number - 1
    fr_pay = round((total_bill / new_number), 2)  # the total bill equally among everyone who's not lucky
    friends_pay = {key: fr_pay for (key, value) in
                   friends.items()}
    lucky_guy = {list_friends[random_friend]: 0}
    friends_pay.update(lucky_guy)
    print(list_friends[random_friend], 'is the lucky one!')
    print(friends_pay)


friend_list(default_value)
print()
if number > 0:
    total_bill = int(input('Enter the total bill value:'))
    print()
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    print()
    if answer == 'Yes':
        lucky(friends, number, total_bill)
    else:
        print()
        print('No one is going to be lucky')
        bill_value(friends, total_bill)
