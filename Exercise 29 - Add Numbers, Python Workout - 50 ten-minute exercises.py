# Our function (sum_numbers) will take a string as an argument;
# for example:
#
# 10 abc 20 de44 30 55fg 40
#
# Given that input, our function should return 100. That’s because
# the function will ignore any word that contains nondigits.

def sum_numbers(string):
    numbers = 0
    string_list = string.split()
    for char in string_list:
        if char.isdigit():
            numbers += int(char)
    print(numbers)

sum_numbers("10 abc 20 de44 30 55fg 40")

#Book solution:

# def sum_numbers(numbers):
#     return sum(int(number)
#     for number in numbers.split()
#     if number.isdigit())
#
#
# print(sum_numbers('1 2 3 a b c 4'))


