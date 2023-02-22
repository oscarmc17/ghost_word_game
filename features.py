import random

# Defining player names
player1 = "Player 1"
player2 = "Player 2"

# .read() reads the list, splitlines() splits a string into a list where each line is a list item. Split at line breaks.


def open_wordlist():
    with open("wordlist.txt", "r") as f:
        return f.read().splitlines()

wordlist = open_wordlist()

# randomly chooses which player goes first
current_player = random.choice([player1, player2])

# Define the current word
word = ""

while True:
    # Prompt current player to enter a letter
    letter = input(f"{current_player} enter a letter: ").lower()

    # letter validation for longer than 1 char or if num.
    if len(letter) > 1 or not letter.isalpha():
        print('Invalid input. Please enter a single letter.')
        continue

    # Check if letter forms the beginning of a valid word
    valid_word_found = False
    for w in wordlist:
        if w.startswith(word+letter):
            valid_word_found = True
            break
    
    # Switch to current player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
