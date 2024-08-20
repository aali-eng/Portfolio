# In this exercise, you can assume that your Python program contains
# a list of integers. We want to print the number of different integers
# contained within that list. Thus, consider the following:
# numbers = [1, 2, 3, 1, 2, 3, 4, 1]
# With the definition provided, running len(numbers) will return 7,
# because the list contains seven elements. How can we get a result
# of 4, reflecting the fact that the list contains four different
# values? Write a function, called how_many_different_numbers, that
# takes a single list of integers and returns the number of different
# integers it contains.

from collections import Counter

def how_many_different_numbers(list):
    counter_object = Counter(list)
    rez = len(counter_object.keys())
    print(rez)

numbers = [1, 2, 3, 1, 2, 3, 4, 1]
how_many_different_numbers(numbers)

#Book solution:

# def how_many_different_numbers(numbers):
#     unique_numbers = set(numbers)
#     return len(unique_numbers)
#
#
# print(how_many_different_numbers([1, 2, 3, 1,
#                                   2, 3, 4, 1]))



