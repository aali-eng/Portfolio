# Implement BigBowl for this exercise, such that the only difference
# between it and the Bowl class we created earlier is that it can have
# five scoops, rather than three. And yes, this means that you should
# use inheritance to achieve this goal. You can modify Scoop and Bowl
# if you must, but such changes should be minimal and justifiable.

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)


    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


class BigBowl(Bowl):
    max_scoops = 5

    def __init__(self, scoops):
        super().__init__(scoops)


    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < BigBowl.max_scoops:
                self.scoops.append(one_scoop)


    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)
print(b)
print("\n")

b2 = BigBowl()
b2.add_scoops(s1, s2, s3, s4)

print(b2)


# Book Solution:
#
# def __init__(self, flavor):
#     self.flavor = flavor
#
#
# class Bowl():
#     max_scoops = 3
#
#     def __init__(self):
#         self.scoops = []
#
#     def add_scoops(self, *new_scoops):
#         for one_scoop in new_scoops:
#             if len(self.scoops) < self.max_scoops:
#             self.scoops.append(one_scoop)
#
#
# def __repr__(self):
#     return '\n'.join(s.flavor for s in self.scoops)
#
#
# class BigBowl(Bowl):
#     max_scoops = 5
#
# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('persimmon')
# s4 = Scoop('flavor 4')
# s5 = Scoop('flavor 5')
#
# bb = BigBowl()
# bb.add_scoops(s1, s2)
# bb.add_scoops(s3)
# bb.add_scoops(s4, s5)
# print(bb)

