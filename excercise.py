# Define player names
import random
player1 = "Player 1"
player2 = "Player 2"

# Open wordlist and store words in a list
def open_wordlist():
    with open("wordlist.txt", "r") as f:
        return f.read().splitlines()


wordlist = open_wordlist()


# Randomly choose which player starts
current_player = random.choice([player1, player2])

