# What’s the task here? Well, you might have noticed a flaw in our Bowl class,
# one that children undoubtedly love and their parents undoubtedly hate:
# you can put as many Scoop objects in a bowl as you like. Let’s make the
# children sad, and their parents happy, by capping the number of scoops
# in a bowl at three. That is, you can add as many scoops in each call to
# Bowl.add_scoops as you want, and you can call that method as many times
# as you want--but only the first three scoops will actually be added.
# Any additional scoops will be ignored.

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


