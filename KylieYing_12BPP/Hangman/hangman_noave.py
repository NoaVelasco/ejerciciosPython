# Python 3.10.2, UTF-8
# Copyright (c) 2022, Noa Velasco

import random

# The game get words from a txt file and appends them in a list.
words = []
with open("lemario.txt", encoding="utf-8") as f:
    for word in f.read().split('\n'):
        if 8 > len(word) > 5:
            words.append(word)

# Set the number of lives.
lives = 8

# 1 word from the list is chosen randomly.
guess_word = random.choice(words)

# We need an dashed version of the word and a list of used letters.
dashed = ["-"] * len(guess_word)
letters_played = []


# If we have more than one match letter>word:
def refindall(l_list, l, string, n):
    """Uses find recursively the whole string
    and return a list with all the indexes of the matched letters."""
    while string.find(l, n) != -1:
        add = string.find(l, n)
        l_list.append(add)
        n = add + 1
    return l_list


while lives > 0:
    # present to the player the number of lives and the word to guess.
    print(
        f"You have {lives} lives left and you have used these letters: \
{' '.join(letters_played).upper()}")
    print("Current word: ", end='')
    for d in dashed:
        print(d.upper(), end=' ')
    # ask for a letter
    letter = input("\n\nGuess a letter: ")
    # check if the letter is correct, incorrect or if it's repeated.
    # repeated -> warning and bucle
    if letter in letters_played:
        print("You have already use that letter. Guess another letter.")
    else:
        # correct -> set the letter in its place and
        letters_played.append(letter)
        # check if win_game is reached -> congratulations. If not -> bucle
        if letter in guess_word:
            matches = []
            refindall(matches, letter, guess_word, 0)
            for i in matches:
                dashed[i] = letter
                if "-" not in dashed:
                    print(
                        f"\nCongratulations! You guessed the word {guess_word.upper()}!!")
        # incorrect -> -1 live and
        else:
            print(f"\nYour letter [{letter.upper()}] is not in the word.")
            lives -= 1
            # check if lose_game is reached -> shame. If not -> bucle
            if lives == 0:
                print(
                    f"\nOh, no! You died. :( The word was {guess_word.upper()}.")
