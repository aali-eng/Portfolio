# Write your code here
supply = {
    "water": 400,
    "milk": 540,
    "beans": 120,
    "cups": 9,
    "money": 550
}

espresso = {
    "water": 250,
    "milk": 0,
    "beans": 16,
    "cups": 1,
    "money": 4
}

latte = {
    "water": 350,
    "milk": 75,
    "beans": 20,
    "cups": 1,
    "money": 7
}

cappuccino = {
    "water": 200,
    "milk": 100,
    "beans": 12,
    "cups": 1,
    "money": 6
}


def show_supply():
    print(f"""
    The coffee machine has:
    {supply["water"]} ml of water
    {supply["milk"]} ml of milk
    {supply["beans"]} g of coffee beans
    {supply["cups"]} disposable cups
    {supply["money"]} of money
    """)


def calculate_buy(var):
    global supply
    if var == "1":
        if supply["water"] >= espresso["water"] and supply["beans"] >= espresso["beans"]:
            print("I have enough resources, making you a coffee!")
            supply = {
                key: supply[key] -
                espresso.get(
                    key,
                    0) for key in supply}
            supply["money"] += espresso["money"] * 2
        else:
            if supply["water"] < espresso["water"]:
                print("Sorry, not enough water!")
            elif supply["beans"] >= espresso["beans"]:
                print("Sorry, not enough beans!")
    elif var == "2":
        if supply["water"] >= latte["water"] and supply["milk"] >= latte["milk"] and supply["beans"] >= latte["beans"]:
            print("I have enough resources, making you a coffee!")
            supply = {key: supply[key] - latte.get(key, 0) for key in supply}
            supply["money"] += latte["money"] * 2
        else:
            if supply["water"] < latte["water"]:
                print("Sorry, not enough water!")
            elif supply["milk"] < latte["milk"]:
                print("Sorry, not enough milk!")
            elif supply["beans"] >= latte["beans"]:
                print("Sorry, not enough beans!")
    elif var == "3":
        if supply["water"] >= cappuccino["water"] and supply["milk"] >= cappuccino["milk"] and supply["beans"] >= cappuccino["beans"]:
            print("I have enough resources, making you a coffee!")
            supply = {
                key: supply[key] -
                cappuccino.get(
                    key,
                    0) for key in supply}
            supply["money"] += cappuccino["money"] * 2
        else:
            if supply["water"] < cappuccino["water"]:
                print("Sorry, not enough water!")
            elif supply["milk"] < cappuccino["milk"]:
                print("Sorry, not enough milk!")
            elif supply["beans"] >= cappuccino["beans"]:
                print("Sorry, not enough beans!")


def calculate_fill(water, milk, beans, cups):
    global supply
    supply = {
        "water": supply["water"] + water,
        "milk": supply["milk"] + milk,
        "beans": supply["beans"] + beans,
        "cups": supply["cups"] + cups,
        "money": supply["money"],
    }


def operations():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            option = input(
                "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            if option == "1":
                calculate_buy("1")
            elif option == "2":
                calculate_buy("2")
            elif option == "3":
                calculate_buy("3")
            elif option == "back":
                operations()
                break
        elif action == "fill":
            calculate_fill(
                int(input("Write how many ml of water you want to add: ")),
                int(input("Write how many ml of milk you want to add: ")),
                int(input("Write how many grams of coffee beans you want to add: ")),
                int(input("Write how many disposable cups you want to add: ")))
        elif action == "take":
            cash = supply["money"]
            print(f"I gave you ${cash}")
            supply["money"] = 0

        elif action == "remaining":

            show_supply()

        elif action == "exit":

            break


if __name__ == '__main__':

    operations()
