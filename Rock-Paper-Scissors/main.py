import random

variants = ['paper', 'rock', 'scissors', 'water', 'dragon', 'devil', 'gun', 'fire', 'snake', 'human', 'tree', 'wolf',
            'sponge', 'air', 'lightning']
win_conditions = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

score = 0
rating: int = 0

user_name = input('Enter your name:')
print(f'Hello, {user_name}')
game_mode = input()
if game_mode.strip() == "":
    variants = ["rock", "paper", "scissors"]
else:
    variants = game_mode.split(",")
print("Okay, let's start")


file = open("rating.txt")
for line in file:
    name, score = line.split(" ")
    if name == user_name:
        rating = int(score)


def game(user_hand):
    global rating
    computer_hand = random.choice(variants)
    if computer_hand == user_hand:
        rating += 50
        print(f'There is a draw ({computer_hand})')
        return rating
    elif computer_hand in win_conditions[user_hand]:
        rating += 100
        print(f'Well done. The computer chose {computer_hand} and failed')
        return rating
    else:
        print(f'Sorry, but the computer chose {computer_hand}')


while True:
    user_hand = input()
    if user_hand == '!exit':
        print('Bye!')
        break
    elif user_hand in win_conditions:
        game(user_hand)
        continue
    elif user_hand == '!rating':
        print('Your rating:', rating)
    else:
        print('Invalid input')
        continue
file.close()
