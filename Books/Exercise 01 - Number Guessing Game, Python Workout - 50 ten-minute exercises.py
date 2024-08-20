# Write a function (guessing_game) that takes no arguments. When run, the function
# chooses a random integer between 0 and 100 (inclusive). Then ask the user to guess
# what number has been chosen. Each time the user enters a guess, the program indicates
# one of the following: Too high Too low Just right If the user guesses correctly,
# the program exits. Otherwise, the user is asked to try again. The program only
# exits after the user guesses correctly.

import random

def guessing_game():
    random_int = random.randint(0, 100)
    game = True
    while game:
        guess_number = int(input("Guess the number: "))
        if guess_number > random_int:
            print("Too high")
        elif guess_number < random_int:
            print("Too low")
        else:
            print("Just right")
            game = False



guessing_game()
