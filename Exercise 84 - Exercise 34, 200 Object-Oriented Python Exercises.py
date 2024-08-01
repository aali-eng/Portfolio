#What is the use of a constructor?

"""
Constractor is the first method that is called when variables are created. It's named __init__
and it takes "self" as the first argument, which is a reference to the instance being constructed,
and the rest of arguments provided by the programmer.
Example:

Person("Alice",33,"Programmer") # Constructor method

obj = Person() # Regular method
obj.name = "Alice"
obj.age = 33
obj.job = "Programmer"
"""