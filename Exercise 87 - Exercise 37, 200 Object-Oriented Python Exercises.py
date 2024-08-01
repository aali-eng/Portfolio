# Create 50 objects of the following class and set the variables
#
# class Animal:
#      def getLegs(self):
#          return legs
#      def getArms(self):
#          return arms


# Book solution:

class Animal:
     legs = 2
     arms = 2

     def getLegs(self):
         return self.legs

     def getArms(self):
         return self.arms

animals = []
for i in range(0,50):
     obj = Animal()
     animals.append(obj)

print(animals)