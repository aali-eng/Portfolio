import pydoc, re

obj = pydoc.render_doc(classmethod)
variables = {}


def LetterAndNumber(input):
    return input.isalnum() and not input.isalpha() and not input.isdigit()


def identifier(obj):
    global inv_char

    inv_char = 0

    for char in list("".join(obj[0])):
        if char.isdigit():
            inv_char = 1
            print("Invalid identifier")

    if inv_char == 0:
        if obj[1].isdigit():
            variables[obj[0]] = obj[1]
        if obj[1].isalpha():
            if obj[1] in variables:
                variables[obj[0]] = variables[obj[1]]
            else:
                print("Unknown variable")
        if LetterAndNumber(obj[1]) is True:
            print("Invalid assignment")

    inv_char = 0


def program():

    while True:
        num = input()

        if "=" in num and num.count("=") == 1:

            num_list = num.split()
            if len(num_list) > 1:
                if num_list[0].endswith("="):
                    num_list[0] = num_list[0].replace("=", "")
                    identifier(num_list)

                elif num_list[1].startswith("=") and len(num_list[1]) > 1:
                    num_list[1] = num_list[1].replace("=", "")
                    identifier(num_list)
                elif num_list[1] == "=":
                    num_list.remove("=")
                    identifier(num_list)

            elif len(num_list) == 1:
                num_list = num.split("=")
                identifier(num_list)

        elif "=" not in num and num != "/help":
            num_list = num.split()
            if len(num_list) == 1:
                if num in variables:
                    print(variables[num])
                elif num.isalnum() and not num.isdigit() and not num.isalpha():
                    print("Invalid identifier")
                elif num not in variables and "+" not in num and "-" not in num and num.isdigit() == False and num != "/help":
                    print("Unknown variable")

        if "+" in num or "-" in num:

            if num.endswith("+") or num.endswith("-"):
                print("Invalid expression")
            elif num.startswith("+") and len(num.split()) == 1:
                print(num[1:])
            elif num.startswith("-") and len(num.split()) == 1:
                print(num)
            elif len(num.split()) == 1:
                print(num)
            elif num == "":
                pass

            else:
                if num.count("=") == 0:
                    for key, value in variables.items():
                        num = re.sub(key, value, num)
                    for key, value in variables.items():
                        num = re.sub(key, value, num)
                    print(eval(num))

        if num.count("=") > 1:
            print("Invalid assignment")

        if num == "":
            pass
        elif num == "/exit":
            print("Bye!")
            break
        elif num == "/help":
            print(obj)
        elif num.startswith("/") and num != "/exit" and num != "/help":
            print("Invalid command")




program()