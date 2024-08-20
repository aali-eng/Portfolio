# Define a class, Circle, that takes two arguments when defined: a sequence
# and a number. The idea is that the object will then return elements the
# defined number of times. If the number is greater than the number of
# elements, then the sequence repeats as necessary. You should define
# the class such that it uses a helper (which I call CircleIterator).
# Here’s an example:
#
# c = Circle('abc', 5)
# print(list(c))


class Circle:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number

    def __iter__(self):
        n = len(self.sequence)
        return (self.sequence[x % n] for x in range(self.number))


