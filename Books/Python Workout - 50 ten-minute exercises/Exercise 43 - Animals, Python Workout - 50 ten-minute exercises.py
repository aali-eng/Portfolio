# For the purposes of these exercises, you are the director of IT at a zoo.
# The zoo contains several different kinds of animals, and for budget reasons,
# some of those animals have to be housed alongside other animals. We will
# represent the animals as Python objects, with each species defined as a
# distinct class. All objects of a particular class will have the same species
# and number of legs, but the color will vary from one instance to another.
#  We can thus create a white sheep:
# s = Sheep('white')
# I can similarly get information about the animal back from the object by
# retrieving its attributes:
# print(s.species)
# print(s.color)
# print(s.number_of_legs)
# If I convert the animal to a string (using str or print), I’ll get back a string
# combining all of these details.

class Sheep:
    def __init__(self, color):
        self.species = 'sheep'
        self.color = color
        self.number_of_legs = 4

class Wolves:
    def __init__(self, color):
        self.species = 'wolve'
        self.color = color
        self.number_of_legs = 4

class Snakes:
    def __init__(self, color):
        self.species = 'snake'
        self.color = color
        self.number_of_legs = 0

class parrots:
    def __init__(self, color):
        self.species = 'parrot'
        self.color = color
        self.number_of_legs = 2

s = Sheep('white')
print(s.species)
print(s.color)
print(s.number_of_legs)

# Book solution:

# class Animal():
#     def __init__(self, color, number_of_legs):
#
#         self.species = self.__class__.__name__
#         self.color = color
#         self.number_of_legs = number_of_legs
#
#
# def __repr__(self):
#     return f'{self.color} {self.species}, {self.number_of_legs} legs'
#
#
# class Wolf(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
#
#
# class Sheep(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
#
#
# class Snake(Animal):
#     def __init__(self, color):
#         super().__init__(color, 0)
#
#
# class Parrot(Animal):
#     def __init__(self, color):
#         super().__init__(color, 2)
#
#
# wolf = Wolf('black')
# sheep = Sheep('white')
# snake = Snake('brown')
# parrot = Parrot('green')
#
# print(wolf)
# print(sheep)
# print(snake)
# print(parrot)
