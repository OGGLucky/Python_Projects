import random
import re

losts = 0
wins = 0

print('H A N G M A N')
def game():
    global losts, wins
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    choose = input()

    if choose == 'play':
        wordlist = 'python', 'java', 'swift', 'javascript'
        random.seed()
        random_word = random.choice(wordlist)
        attempts = 8
        # letter_word = list(random_word)
        # print(random_word)

        # a = index.random_word[letter]

        word = ("-" * (len(random_word)))
        list(word)
        print(''.join(word))

        letter_box = set()

        while attempts != 0:
            if random_word != word:  # if word not unraveled
                letter = input("Input a letter:")
                if len(letter) != 1:
                    print('Please, input a single letter.')
                    print(word)
                    continue
                elif not re.search(r'[a-z]', letter):
                    print('Please, enter a lowercase letter from the English alphabet.')
                    print(word)
                    continue
                if letter in letter_box:
                    print("You've already guessed this letter.")
                    print(word)
                    continue
                letter_box.add(letter)

                if letter in random_word:
                    for i in random_word:
                        if letter == i:
                            index_letter = random_word.find(letter)
                            word = word[:index_letter] + letter + word[index_letter + 1:]
                        else:
                            for j in random_word:
                                if letter == j:
                                    index_letter = random_word.rfind(letter)
                                    word = word[:index_letter] + letter + word[index_letter + 1:]
                    print(word)
                else:
                    if attempts != 0:
                        print("That letter doesn't appear in the word.")
                        attempts -= 1
                        print(word)
                        continue
                    elif attempts == 0:
                        losts += 1
                        print('You lost!')
                        game()
                        break
            else:
                wins += 1
                print(f'You guessed the word {word}!')
                print('You survived!')
                game()
                break

        if attempts == 0:
            losts += 1
            print('You lost!')
            game()

    elif choose == exit:
        exit(0)

    elif choose == 'results':
        print(f'You won: {wins} times.')
        print(f'You lost: {losts} times.')
        game()
game()
