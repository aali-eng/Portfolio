# This exercise, the result of which you’ll use in the next one,
# asks that you create a dict whose keys are the (lowercase) letters
# of the English alphabet, and whose values are the numbers ranging
# from 1 to 26. And yes, you could simply type {'a':1, 'b':2, 'c':3}
# and so forth, but I’d like you to do this with a dict comprehension.


import functools

def dict_creator():

    alph = functools.reduce(lambda s, i: s + chr(i), range(97, 97 + 26), '')
    dict = {k:v for (k,v) in zip(alph, range(1, 27))}

    print(dict)

dict_creator()


# Book solution:
#
# import string
#
# def gematria_dict():
#     return {char: index
#     for index, char
#     in enumerate(string.ascii_lowercase,
#                  1)}
#
#
# print(gematria_dict())
