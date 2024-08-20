# Write a function, dictdiff, that takes two dicts as arguments.
# The function returns a new dict that expresses the difference
# between the two dicts. If there are no differences between the dicts,
# dictdiff returns an empty dict. For each key-value pair that differs,
# the return value of dictdiff will have a key-value pair in which the value
# is a list containing the values from the two different dicts. If one of
# the dicts doesn’t contain that key, it should contain None.

def dictdiff(dict1, dict2):
    dict_set = dict1.keys() | dict2.keys()
    output = {}
    for key in dict_set:
        if dict1.get(key) != dict2.get(key):
            output[key] = [dict1.get(key), dict2.get(key)]
    return output

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4, 'd':5}

print(dictdiff(d1, d2))
