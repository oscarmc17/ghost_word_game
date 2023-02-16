import random

split = []

# .read() reads the list, splitlines() splits a string into a list where each line is a list item. Split at line breaks.


def open_wordlist():
    with open("wordlist.txt", "r") as f:
        return f.read().splitlines()


wordlist = open_wordlist()


while True:

    letter = input(f" enter a letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print('Invalid input. Please enter a single letter.')
        continue
