# Write a function that takes a list of lists (just one element deep)
# and returns a flat, one-dimensional version of the list. Thus,
# invoking flatten([[1,2], [3,4]]) will return [1,2,3,4]

def flattener(list):
    new_list = []
    for items in list:
        for numbers in items:
            new_list.append(numbers)
    print(new_list)

flattener([[1,2], [3,4]])




# Book solution:

# def flatten(mylist):
#     return [one_element
#             for one_sublist in mylist
#     for one_element in one_sublist]
#
#
# print(flatten([[1, 2], [3, 4]]))
