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

# Strikes counter for each player
player1_strikes = 0
player2_strikes = 0

# Define the current word
word = ""

# Define round counter
round_count = 1
game = True

print(f"Round {round_count}")

while game:
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

        # If valid word not found, count as strike and repeat turn
        if not valid_word_found:
            print(
                "Invalid move. Please enter a letter that forms the beginning of a valid word.")
            if current_player == player1:
                player1_strikes += 1
                if player1_strikes >= 3:
                    print(f"{player2} wins! {player1} has struck out!")
                    break
            else:
                player2_strikes += 1
                if player2_strikes >= 3:
                    print(f"{player1} wins! {player2} has struck out!")
                    break
            continue

        # Add the letter to the current word after validations
        word += letter

        # Check if player has completed a valid word of at least 3 letters
        if len(word) >= 3 and word in wordlist:
            if current_player == player1:
                print(f'{player2} wins! {player1} has spelled {word}')
            else:
                print(f'{player1} wins! {player2} has spelled {word}')
            break

        # Switch to current player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

    # Prompt to play another round
    play_again = input("Play another round? (y/n): ").lower()
    if play_again == 'n':
        game = False
    else:
        word = ""
        player1_strikes = 0
        player2_strikes = 0
        current_player = random.choice([player1, player2])
        round_count += 1
        print(f"\nRound {round_count}")
