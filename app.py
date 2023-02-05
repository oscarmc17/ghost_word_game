import random


split = []
current_word = []
# player1 = ''
# player2 = ''

# open_wordlist function that opens wordlist.txt, splits every word into a new list.
def open_wordlist():
    with open("wordlist.txt", "r") as f:
        split.extend(f.read().splitlines())
    # print(split)
    
open_wordlist()


def start():
    # open_wordlist()

    while True:
        while True:
            try:
                player1 = input("Player 1 enter a letter: ")
                if player1.isdigit() or len(player1) > 1:
                    raise ValueError(
                        'Input contains digits or more than one character.')
                break
            except ValueError as e:
                print(e)
                print("Try again.")
        current_word.append(player1)

        while True:
            try:
                player2 = input("Player 2 enter a letter: ")
                if player2.isdigit() or len(player2) > 1:
                    raise ValueError(
                        'Input contains digits or more than one character.')
                break
            except ValueError as e:
                print(e)
                print("Try again.")
        current_word.append(player2)

        # break
        
        word = ''.join(current_word)
        if word in split:
            print(word)
            print('We in here')
            break
        # print(word)


start()
