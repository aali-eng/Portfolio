# In this exercise, I want you to create a new constant dict, called MENU,
# representing the possible items you can order at a restaurant. The keys
# will be strings, and the values will be prices (i.e., integers). You
# should then write a function, restaurant, that asks the user to enter
# an order: If the user enters the name of a dish on the menu, the program
# prints the price and the running total. It then asks the user again for
# their order. If the user enters the name of a dish not on the menu,
# the program scolds the user (mildly). It then asks the user again
# for their order. If the user enters an empty string, the program
# stops prompting and prints the total amount. For example, a session
# with the user might look like this: 
# Order: sandwich
# sandwich costs 10, total is 10
# Order: tea
# tea costs 7, total is 17
# Order: elephant
# Sorry, we are fresh out of elephant today.
# Order: <enter>
# Your total is 17
# Note that you can always check to see if a key is in a dict with the in operator.
# That returns True or False.


MENU = {'sandwich' : 10,
        'tea': 7,
        'hamburger' : 12,
        'pizza' : 18,
        }

def restaurant():
    total = 0
    order = True
    while order:
        entry = input("What would you like to order? ")
        if entry.lower() in MENU.keys():
            total += MENU[entry]
        elif entry.lower() not in MENU.keys() and entry.lower() != "":
            print(f"Sorry, we are fresh out of {entry} today")
        elif entry.lower() == "":
            print(f"Your total {total}")
            break

restaurant()


