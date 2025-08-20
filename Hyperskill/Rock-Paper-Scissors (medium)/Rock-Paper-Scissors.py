import random

# processing user & game data

def data_handling():
    global options, current_score
    name = input("Enter your name: ")
    while True:
        if name != "rock" and name != "scissors" and name != "paper" and name != "!rating" and name != "!exit":
            print(f"Hello {name}")
            break
        else:
            print(f"{name} is the name of the option chosen by the program")
            name = input("Enter your name: ")

    options_default = ["rock", "paper", "scissors"]
    options = input()
    if options == "":
        options = options_default
    else:
        options = options.split(",")

    print("Okay, let's start")

    with open("rating.txt") as testfile:
        data = testfile.read()
    if name not in data:
        with open("rating.txt", 'a') as testfile:
            testfile.write(name + " 0" + "\n")
            file_entry = name + " 0"
    elif name in data:
        file = open("rating.txt", "r+")
        lines = file.readlines()

        for row in lines:
            if row in lines and row.find(name + " ") == 0:
                file_entry = lines[lines.index(row)]
        file.close()

    name_score_list = file_entry.split()
    current_score = int(name_score_list[1])


# calculating score

def result(var, var2):

    global current_score, user_selection_index

    if user_selection in options:
        user_selection_index = options.index(user_selection)
        options_after_selection = options[user_selection_index + 1:]
        options_before_selection = options[:user_selection_index]
        deck_for_splitting = options_after_selection + options_before_selection
        deck_middle_index = len(deck_for_splitting) // 2
        user_win_deck = deck_for_splitting[deck_middle_index:]

        if computer in user_win_deck:
            print(f"Well done. The computer chose {computer} and failed")
            current_score += 100
        elif user_selection == computer:
            print(f"There is a draw ({user_selection})")
            current_score += 50
        elif computer not in user_win_deck:
            print(f"Sorry, but the computer chose {computer}")
        else:
            print("Invalid input")


# game function

def game():
    global user_selection, computer
    data_handling()
    while True:

        user_selection = input()
        computer = random.choice(options)

        if user_selection in options:
            result(user_selection, computer)
        elif user_selection == "!rating":
            print(f"Your rating: {current_score}")
        elif user_selection not in options and user_selection != "!rating" and user_selection != "!exit":
            print("Invalid input")
        elif user_selection == "!exit":
            print("Bye!")
            break


if __name__ == "__main__":
    game()
