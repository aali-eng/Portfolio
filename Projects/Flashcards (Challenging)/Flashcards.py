# Write your code here
import random

cards_dict = {}


def program():
    while True:
        print("Input the action (add, remove, import, export, ask, exit):")
        action = input()

        def add_cards():
            card = input(f"The card:\n")
            if card in cards_dict:
                while card in cards_dict:
                    print(f'The term "{card}" already exists. Try again:')
                    card = input()
            definition = input(f"The definition:\n")
            if definition in cards_dict.values():
                while definition in cards_dict.values():
                    print(
                        f'The definition "{definition}" already exists. Try again:')
                    definition = input()
            cards_dict[card] = definition
            print(f'The pair ("{card}":"{definition}") has been added')

        def remove():
            card_to_remove = input("Which card?\n")
            if card_to_remove in cards_dict:
                cards_dict.pop(card_to_remove)
                print("The card has been removed.")
            else:
                print(
                    f'''Can't remove "{card_to_remove}": there is no such card.''')

        def import_file():
            global cards_dict
            print("File name:")
            user_input = input()

            try:
                with open(user_input, "r") as file:
                    data = file.read()
                    imported_dict = eval(data)
                    print(f'{len(imported_dict)} cards have been loaded.')

                    for card in cards_dict:
                        if card in imported_dict:
                            cards_dict[card] = imported_dict.get(card)
                            imported_dict.pop(card)

                    cards_dict.update(imported_dict)
                    print(cards_dict)

            except FileNotFoundError:
                print("File not found.")
                program()

        def export():
            file_name = input("File name:\n")
            with open(file_name, 'w') as file:
                file.write(str(cards_dict))
                print(f"{len(cards_dict)} cards have been saved.")

        def ask():
            num = int(input("How many times to ask?\n"))
            dict = {}

            for item in range(num):
                key, value = random.choice(list(cards_dict.items()))
                dict[key] = value

            for term in dict:
                answer = input(f'Print the definition of "{term}":\n')
                if answer == dict[term]:
                    print("Correct!")
                elif answer != dict[term]:
                    if answer in dict.values():
                        obj = "".join([key for key, value in dict.items() if value == answer])
                        print(f'Wrong. The right answer is "{dict[term]}", but your definition is correct for "{obj}".')
                    else:
                        print(f'Wrong. The right answer is "{dict[term]}".')

        if action == "exit":
            print("Bye bye!")
            break
        elif action == "add":
            add_cards()
        elif action == "remove":
            remove()
        elif action == "import":
            import_file()
        elif action == "export":
            export()
        elif action == "ask":
            ask()



program()
