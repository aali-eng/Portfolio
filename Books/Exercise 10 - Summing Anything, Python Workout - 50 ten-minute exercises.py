# This challenge asks you to redefine the mysum function we defined in chapter 1,
# such that it can take any number of arguments. The arguments must all be of the
# same type and know how to respond to the + operator. (Thus, the function should
# work with numbers, strings, lists, and tuples, but not with sets and dicts.)
# The result should be a new, longer sequence of the type provided by the parameters.
# Thus, the result of mysum('abc', 'def') will be the string abcdef, and the result
# of mysum([1,2,3], [4,5,6]) will be the six-element list [1,2,3,4,5,6]. Of course,
# it should also still return the integer 6 if we invoke mysum(1,2,3).



def mysum(*string):
     if not string:
         return string
     else:
         output = string[0]
         for string in string[1:]:
             output += string
             return output


print(mysum("test1", "test2"))
print(mysum([1,2,3], [4,5,6]))
print(mysum(1,2,3))