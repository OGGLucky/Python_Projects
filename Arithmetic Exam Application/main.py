import random

mark = 0


def exam():
    global mark, answer, ans
    for i in range(5):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        oper = random.choice(['+', '-', '*'])
        #  'answer' is a right answer
        if oper == '+':
            answer = a + b
        elif oper == '-':
            answer = a - b
        elif oper == '*':
            answer = a * b
        print(a, oper, b)
        while True:
            try:
                user_answer = int(input())
                if user_answer == answer:
                    mark += 1
                    print("Right!")
                    break
                else:
                    print('Wrong!')
                    break
            except ValueError:
                print('Incorrect format.')
                continue
    print(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.')
    save_answer = input()
    if save_answer == 'yes' or save_answer == 'YES' or save_answer == 'y' or save_answer == 'Yes':
        print('What is your name?')
        name = input()
        if ans == '1':
            level = 'simple operations with numbers 2-9'
        elif ans == '2':
            level = 'integral squares of 11-29'
        result = open('results.txt', 'a')
        result.write(f'{name}: {mark}/5 in level {ans} ({level}).')
        result.close()
        print('The results are saved in "results.txt".')


def hardexam():
    global mark, answer, ans
    for i in range(5):
        a = random.randint(11, 29)
        answer = a * a
        print(a)
        while True:
            try:
                user_answer = int(input())
                if user_answer == answer:
                    mark += 1
                    print("Right!")
                    break
                else:
                    print('Wrong!')
                    break
            except ValueError:
                print('Incorrect format.')
                continue
    print(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.')
    save_answer = input()
    if save_answer == 'yes' or save_answer == 'YES' or save_answer == 'y' or save_answer == 'Yes':
        print('What is your name?')
        name = input()
        if ans == '1':
            level = 'simple operations with numbers 2-9'
        elif ans == '2':
            level = 'integral squares of 11-29'
        result = open('results.txt', 'a')
        result.write(f'{name}: {mark}/5 in level {ans} ({level}).')
        result.close()
        print('The results are saved in "results.txt".')


while True:
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    ans = input() # ans is level
    if ans == '1':
        exam()
        break
    elif ans == '2':
        hardexam()
        break
    else:
        print('Incorrect format.')
        continue
