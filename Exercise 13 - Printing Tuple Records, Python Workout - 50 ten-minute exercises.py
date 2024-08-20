PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Zelenskiy', 3.626),
          ('Jinping', 'Xi', 10.603)]

# For this exercise, write a Python function, format_sort_records,
# that takes the PEOPLE list and returns a formatted string that
# looks like the following:
#
# Trump      Donald      7.85
# Zelenskiy  Vladimir    3.63
# Xi         Jinping    10.60

import operator

def format_sort_records(list_of_tuples):
    output = []
    template = "{1:10} {0:10} {2:5.2f}"
    for person in sorted(list_of_tuples, key=operator.itemgetter(1, 0)): output.append(template.format(*person))
    return output

print('\n'.join(format_sort_records(PEOPLE)))