import random


# Define function for handling guests


def guests():
    # Define function for printing dict with split bill

    def bill(guests, paid_for):
        if paid_for in num_list:
            split_bill = round((total_bill / (num - 1)), 2)
            num_dict = {guest: split_bill for guest in guests}
            num_dict[random_guest] = 0
            print(num_dict)
        else:
            split_bill = round((total_bill / num), 2)
            num_dict = {guest: split_bill for guest in guests}
            print(num_dict)

    num = int(input("Enter the number of friends joining (including you): "))
    num_list = []
    if num > 0:
        for var in range(num):
            var = input()
            num_list.append(var)
        total_bill = int(input("Enter the total bill value: "))
        who_is_paid_for = input(
            'Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
        if who_is_paid_for == "Yes":
            random_guest = random.choice(num_list)
            print(f"{random_guest} is the lucky one!")
            bill(num_list, random_guest)
        else:
            print("No one is going to be lucky")
            bill(num_list, 0)
    else:
        print("No one is joining for the party")


# Call the functon
guests()
