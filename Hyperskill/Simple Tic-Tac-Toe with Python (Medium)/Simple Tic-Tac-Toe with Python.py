string = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

line_1 = " ".join(string[:3])
line_2 = " ".join(string[3:6])
line_3 = " ".join(string[6:])
line_4 = " ".join(string)
grid = [string[:3], string[3:6], string[6:]]

result = ""
result2 = ""
result3 = ""
result4 = ""

count = 0

result_final = ""

print(f"""
---------
| {line_1} |
| {line_2} |
| {line_3} |
---------
""")


def num_input():
    global user_input, coordinates
    while True:
        user_input = input()

        if "".join(user_input.split()).isnumeric() != True:
            print("You should enter numbers!")
        else:
            coordinates = [int(x) - 1 for x in user_input.split()]
            main()
            break


def main():
    global result, count
    while True:
        if len(coordinates) != 2 or coordinates[0] not in range(
                0, 3) or coordinates[1] not in range(0, 3):
            print("Coordinates should be from 1 to 3!")
            num_input()
            break
        elif grid[coordinates[0]][coordinates[1]] != " ":
            print("This cell is occupied! Choose another one!")
            num_input()
            break
        else:
            if count == 0 or count % 2 != 1:
                grid[coordinates[0]][coordinates[1]] = "X"
                count += 1
                print(f"""
---------
| {" ".join(grid[0])} |
| {" ".join(grid[1])} |
| {" ".join(grid[2])} |
---------
""")
                check_result()

                break
            else:
                grid[coordinates[0]][coordinates[1]] = "O"
                count += 1

                print(f"""
---------
| {" ".join(grid[0])} |
| {" ".join(grid[1])} |
| {" ".join(grid[2])} |
---------
""")
            check_result()

            break


def check_result():
    global result, result2, result3, result4, result_final

    if "X X X" in " ".join(
        grid[0]) or "X X X" in " ".join(
        grid[1]) or "X X X" in " ".join(
            grid[2]):
        result = "X wins"
    elif " ".join(grid[0][0]) == "X" and " ".join(grid[1][1]) == "X" and " ".join(grid[2][2]) == "X":
        result = "X wins"
    elif " ".join(grid[0][2]) == "X" and " ".join(grid[1][1]) == "X" and " ".join(grid[2][0]) == "X":
        result = "X wins"
    elif " ".join(grid[0][0]) == "X" and " ".join(grid[1][0]) == "X" and " ".join(grid[2][0]) == "X":
        result = "X wins"
    elif " ".join(grid[0][1]) == "X" and " ".join(grid[1][1]) == "X" and " ".join(grid[2][1]) == "X":
        result = "X wins"
    elif " ".join(grid[0][2]) == "X" and " ".join(grid[1][2]) == "X" and " ".join(grid[2][2]) == "X":
        result = "X wins"

    if "O O O" in " ".join(
        grid[0]) or "O O O" in " ".join(
        grid[1]) or "O O O" in " ".join(
            grid[2]):
        result2 = "O wins"
    elif " ".join(grid[0][0]) == "O" and " ".join(grid[1][1]) == "O" and " ".join(grid[2][2]) == "O":
        result2 = "O wins"
    elif " ".join(grid[0][2]) == "O" and " ".join(grid[1][1]) == "O" and " ".join(grid[2][0]) == "O":
        result2 = "O wins"
    elif " ".join(grid[0][0]) == "O" and " ".join(grid[1][0]) == "O" and " ".join(grid[2][0]) == "O":
        result2 = "O wins"
    elif " ".join(grid[0][1]) == "O" and " ".join(grid[1][1]) == "O" and " ".join(grid[2][1]) == "O":
        result2 = "O wins"
    elif " ".join(grid[0][2]) == "O" and " ".join(grid[1][2]) == "O" and " ".join(grid[2][2]) == "O":
        result2 = "O wins"
    elif result != "X wins" and result2 != "O wins" and " " not in "".join(grid[0]) and \
            " " not in "".join(grid[1]) and " " not in "".join(grid[2]):
        result4 = "Draw"

    result_final = ""

    if result == "X wins" and result2 != "O wins":
        result_final = result
    elif result2 == "O wins" and result != "X wins":
        result_final = result2
    elif result4 == "Draw":
        result_final = result4

    if result_final == "X wins" or result_final == "O wins" or result_final == "Draw":
        print(f"{result_final}")
    else:
        num_input()

num_input()