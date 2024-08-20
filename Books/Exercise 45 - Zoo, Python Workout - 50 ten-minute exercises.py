# Finally, the time has come to create our Zoo object. It will contain
# cage objects, and they in turn will contain animals. Our Zoo class
# will need to support the following operations:
#
# Given a zoo z, we should be able to print all of the cages (with their
# ID numbers) and the animals inside simply by invoking print(z). We should
# be able to get the animals with a particular color by invoking the method
# z.animals_by_color. For example, we can get all of the black animals by
# invoking z.animals_by_color('black'). The result should be a list of Animal
# objects. We should be able to get the animals with a particular number of
# legs by invoking the method z.animals_by_legs. For example, we can get
# all of the four-legged animals by invoking z.animals_by_legs(4). The result
# should be a list of Animal objects. Finally, we have a potential donor to
# our zoo who wants to provide socks for all of the animals. Thus, we need
# to be able to invoke z.number_of_legs() and get a count of the total number
# of legs for all animals in our zoo.
#
# The exercise is thus to create a Zoo class on which we can invoke the following:
#
# z = Zoo()
# z.add_cages(c1, c2)
#
# print(z)
# print(z.animals_by_color('white'))
# print(z.animals_by_legs(4))
# print(z.number_of_legs())


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


class Goat(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


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

class Zoo():

    def __init__(self):
        self.cages = []

    def add_cages(self, *new_cages):
        for cage in new_cages:
            self.cages.append(cage)

    def __repr__(self):
            return '\n'.join(str(one_cage)
                             for one_cage in self.cages)


    def animals_by_color(self, color):

        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]


    def animals_by_legs(self, number_of_legs):

            return [one_animal
                    for one_cage in self.cages
                    for one_animal in one_cage.animals
                    if one_animal.number_of_legs ==
                    number_of_legs]


    def number_of_legs(self):

        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)


wolf = Wolf('black')
sheep = Sheep('white')
parrot = Parrot('green')
goat =  Goat('white')

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(wolf, parrot)

z = Zoo()
z.add_cages(c1, c2)

print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
