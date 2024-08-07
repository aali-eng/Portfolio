# What’s the meaning of the code below?


def update(self, iterable):
     for item in iterable:
         self.items_list.append(item)

__update = update


"""
It wouldn't work, because private values with double underscores can't be updated and the update function
doesn't have parentheses.
"""
