print('How many pencils would you like to use:')

while True:
    try:
        pencil = int(input())
    except ValueError:
        print('The number of pencils should be numeric')
        continue
    if pencil <= 0:
        print('The number of pencils should be positive')
        continue
    break

whos_turn = 0

print('Who will be the first (John, Jack):')
while True:
    first = input()
    if first == 'Jack':
        whos_turn = 1
        break
    elif first == 'John':
        whos_turn = 0
        break
    else:
        print("Choose between 'John' and 'Jack'")
        continue

while True:
    if whos_turn == 0:
        whos_turn = 1
    elif whos_turn == 1:
        whos_turn = 0

    if pencil == 0:
        if whos_turn == 1:
            print('John won!')
            break
        else:
            print('Jack won!')
            break

    print('|' * pencil)
    if whos_turn == 0:
        print("Jack's turn:")
        if pencil % 4 == 0:
            move = 3
            pencil -= move
        elif pencil % 4 == 3:
            move = 2
            pencil -= move
        elif pencil % 4 == 2:
            move = 1
            pencil -= move
        else:
            move = 1
            pencil -= move
        print(move)
        continue
    else:
        print("John's turn!")

    while True:
        try:
            move = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue
        if move <= 0 or move > 3:
            print("Possible values: '1', '2' or '3'")
            continue
        if move > pencil:
            print('Too many pencils were taken')
            continue
        break

    pencil -= move
