# For this exercise, first create a dict of any size, in which
# the keys are unique and the values are also unique. (A key may
# appear as a value, or vice versa.) Here’s an example:
# d = {'a':1, 'b':2, 'c':3}
# Turn the dict inside out, such that the keys and the values are reversed.


def dict_reverser(d):

    dict_keys = {key for key in d.keys()}
    dict_values = {value for value in d.values()}

    new_dict = {k:v for (k,v) in zip(dict_values, dict_keys)}
    print(new_dict)

d = {'a':1, 'b':2, 'c':3}
dict_reverser(d)


#Book solution:

# def flipped_dict(a_dict):
#     return {value: key
#             for key, value in a_dict.items()}
#
#     print(flipped_dict({'a': 1, 'b': 2, 'c': 3}))


