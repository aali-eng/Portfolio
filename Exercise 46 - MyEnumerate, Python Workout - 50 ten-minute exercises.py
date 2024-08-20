# Create your own MyEnumerate class, such that someone can
# use it instead of enumerate. It will need to return a tuple
# with each iteration, with the first element in the tuple being
# the index (starting with 0) and the second element being the
# current element from the underlying data structure. Trying to
# use MyEnumerate with a noniterable argument will result in an error.

# Book solution:

class MyEnumerate():
    def __init__(self, data):


        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = (self.index, self.data[self.index])
        self.index += 1
        return value

for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')
