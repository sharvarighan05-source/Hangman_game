import random

# My 5 words
words = ["python", "github", "code", "intern", "player"]

# Pick the random word
secret_word = random.choice(words)

# Make the blanks list
# If word is code, it makes ['_', '_', '_', '_']
board = []
for letter in secret_word:
    board.append("_")

# Game setup variables
turns = 6
wrong_guesses = []

print("Welcome to Hangman!")

# The main loop that keeps the game going
while turns > 0 and "_" in board:
    print("\nWord to guess:")
    print(board)
    print("Turns left:", turns)
    print("Wrong letters:", wrong_guesses)

    guess = input("Guess a letter: ")
    guess = guess.lower()

    # Check if letter is in the word
    if guess in secret_word:
        print("Correct!")
        # Find where the letter goes and replace the underscore
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                board[i] = guess
    else:
        print("Incorrect!")
        wrong_guesses.append(guess)
        turns = turns - 1

# Check if won or lost
if "_" not in board:
    print("You win! The word was:", secret_word)
else:
    print("You lose! The word was:", secret_word)
