import random


split = []
current_word = []
player1_strikes = 0
player2_strikes = 0


def open_wordlist():
    with open("wordlist.txt", "r") as f:
        split.extend(f.read().splitlines())


open_wordlist()


def start():
    global player1_strikes
    global player2_strikes
    
    while True:
        while True:
            try:
                player1 = input("Player 1 enter a letter: ")
                if player1.isdigit() or len(player1) > 1:
                    player1_strikes += 1
                    raise ValueError(
                        'Input contains digits or more than one character. Player 1 strike {}'.format(player1_strikes))
                break
            except ValueError as e:
                print(e)
                print("Try again.")

        current_word.append(player1)

        while True:
            try:
                player2 = input("Player 2 enter a letter: ")
                if player2.isdigit() or len(player2) > 1:
                    player2_strikes += 1
                    raise ValueError(
                        'Input contains digits or more than one character. Player 2 strike {}'.format(player2_strikes))
                break
            except ValueError as e:
                print(e)
                print("Try again.")

        current_word.append(player2)

        word = ''.join(current_word)
        if word in split:
            print("The word '{}' is a valid word. Player {} loses!".format(
                word, 2 if player1_strikes > player2_strikes else 1))
            break
        elif player1_strikes == 3 or player2_strikes == 3:
            print("Player {} loses by accumulating 3 strikes.".format(
                2 if player1_strikes > player2_strikes else 1))
            break


start()
