PEOPLE = [{'first':'Joe', 'last':'Biden',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Zelenskiy',
    'email':'president@gvt.ua'},
{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'}
 ]

# alphabetize_names, that assumes the existence of a PEOPLE
# constant defined as shown in the code. The function should
# return the list of dicts, but sorted by last name and then
# by first name.

import operator

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts,
        key=operator.itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))
