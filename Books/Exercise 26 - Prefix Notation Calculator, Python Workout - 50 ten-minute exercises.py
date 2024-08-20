# For this exercise, I want you to write a function (calc) that expects
# a single argument--a string containing a simple math expression in
# prefix notation--with an operator and two numbers. Your program will
# parse the input and produce the appropriate output. For our purposes,
# it’s enough to handle the six basic arithmetic operations in Python:
# addition, subtraction, multiplication, division (/), modulus (%), and
# exponentiation (**). The normal Python math rules should work, such that
# division always results in a floating-point number. We’ll assume, for
# our purposes, that the argument will only contain one of our six operators
# and two valid numbers. But wait, there’s a catch--or a hint, if you prefer:
# you should implement each of the operations as a separate function,
# and you shouldn’t use an if statement to decide which function should
# be run. Another hint: look at the operator module, whose functions
# implement many of Python’s operators.

import re

def calc(string):
    numbers = re.findall(r"\d+", string)
    operator = re.findall(r"\W+", string)
    rez = eval(f"{int(numbers[0])} {operator[0]} {int(numbers[1])}")
    return rez

string = "2 % 4"

print(calc(string))

#Book solution:
#
# import operator
#
# def calc(to_solve):
#     operations = {'+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv,
#     '**': operator.pow,
#     '%': operator.mod}
#
#     op, first_s, second_s = to_solve.split()
#     first = int(first_s)
#     second = int(second_s)
#
#     return operations[op](first, second)
#
#     print(calc('+ 2 3'))

