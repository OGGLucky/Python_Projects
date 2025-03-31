M = float()

msg = ["Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def values_check(x, oper, y):
    x = str(x)
    y = str(y)
    if x.isalpha():
        print("Do you even know what numbers are? Stay focused!")
    elif y.isalpha():
        print("Do you even know what numbers are? Stay focused!")
    elif oper.isnumeric() or oper.isalpha():
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    else:
        return True


def check(x, y, oper):
    v1 = x
    v2 = y
    v3 = oper
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == '*':
         msg += " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += " ... very, very lazy"
    if msg != '':
        msg = "You are" + msg
    else:
        return print(msg)
    return print(msg)


while True:

    print("Enter an equation")
    x, oper, y = input().split()
    if x == 'M' and y == 'M':
        x = M
        y = M
    elif x == 'M':
        x = M
        print('ready')
    elif y == 'M':
        y = M
        print('ready')

    if values_check(x, oper, y):
        x = float(x)
        y = float(y)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/':
            if y == 0:
                check(x, y, oper)
                print('Yeah... division by zero. Smart move...')
                continue
            else:
                result = x / y
        check(x, y, oper)
        print(float(result))
        print('Do you want to store the result? (y / n):')
        answer_store = input()
        if answer_store == 'y':
            if is_one_digit(result):
                msg_index = 0
                while msg_index < 3:
                    print(msg[msg_index])
                    answer_store_dig = input()
                    if answer_store_dig == 'y':
                        if msg_index < 2:
                            msg_index += 1
                            continue
                        else:
                            M = result
                            print("Do you want to continue calculations? (y / n):")
                            answer = input()
                            if answer == 'y':
                                break
                            elif answer == 'n':
                                break
                    else:
                        print("Do you want to continue calculations? (y / n):")
                        answer = input()
                        if answer == 'y':
                            break
                        elif answer == 'n':
                            break
            else:
                M = result
                print("Do you want to continue calculations? (y / n):")
                answer = input()
                if answer == 'y':
                    continue
                elif answer == 'n':
                    break
        elif answer_store == 'n':
            print("Do you want to continue calculations? (y / n):")
            answer = input()
            if answer == 'y':
                continue
            elif answer == 'n':
                break
