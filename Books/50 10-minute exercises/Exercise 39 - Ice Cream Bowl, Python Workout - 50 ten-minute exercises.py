# That said, composition is also an important technique, because
# it lets us create larger objects out of smaller ones. I can create
# a car out of a motor, wheels, tires, gearshift, seats, and the like.
# I can create a house out of walls, floors, doors, and so forth.
# Dividing a project up into smaller parts, defining classes that
# describe those parts, and then joining them together to create
# larger objects--that’s how object-oriented programming works.
# In this exercise, we’re going to see a small-scale version of that.
# In the previous exercise, we created a Scoop class that represents
# one scoop of ice cream. If we’re really going to model the real world,
# though, we should have another object into which we can put the scoops.
# I thus want you to create a Bowl class, representing a bowl into which
# we can put our ice cream.

class Scoops:
    def __init__(self, scoops):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        self.scoops.append(new_scoops)
        print(self.scoops)


# Book solution:
#
# class Scoop():
#     def __init__(self, flavor):
#         self.flavor = flavor
#
#
# class Bowl():
#     def __init__(self):
#         self.scoops = []
#
#         def add_scoops(self, *new_scoops):
#
#         for one_scoop in new_scoops:
#             self.scoops.append(one_scoop)
#
#     def __repr__(self):
#         return '\n'.join(s.flavor for s in self.scoops)
#
# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('persimmon')
#
# b = Bowl()
# b.add_scoops(s1, s2)
# b.add_scoops(s3)
# print(b)
