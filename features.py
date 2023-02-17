import random

#Defining player names
player1 = "Player 1"
player2 = "Player 2"

# .read() reads the list, splitlines() splits a string into a list where each line is a list item. Split at line breaks.
def open_wordlist():
    with open("wordlist.txt", "r") as f:
        return f.read().splitlines()

wordlist = open_wordlist()

# randomly chooses which player goes first
current_player = random.choice([player1, player2])
# print(current_player)

while True:
    # Prompt current player to enter a letter
    letter = input(f"{current_player} enter a letter: ").lower()

    # letter validation for longer than 1 char or if num.
    if len(letter) > 1 or not letter.isalpha():
        print('Invalid input. Please enter a single letter.')
        continue

    
    

