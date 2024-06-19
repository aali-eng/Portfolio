# Now that we’ve created some animals, it’s time to put them into cages.
# For this exercise, create a Cage class, into which you can put one or
# more animals, as follows:
#
# c1 = Cage(1)
# c1.add_animals(wolf, sheep)
#
# c2 = Cage(2)
# c2.add_animals(snake, parrot)
#
# When you create a new Cage, you’ll give it a unique ID number. (The
# uniqueness doesn’t need to be enforced, but it’ll help us to distinguish
# among the cages.) You’ll then be able to invoke add_animals on the new cage,
# passing any number of animals that will be put in the cage. I also want you
# to define a __repr__ method so that printing a cage prints not just the cage
# ID, but also each of the animals it contains.

class Animal():
    def __init__(self, color, number_of_legs):

        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs


def __repr__(self):
    return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class Cage():

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):

        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

print(c1)
print(c2)