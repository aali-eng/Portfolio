# While itertools.chain is convenient and clever, it’s not that
# hard to implement. For this exercise, that’s precisely what you should do:
# implement a generator function called mychain that takes any number of
# arguments, each of which is an iterable. With each iteration, it should
# return the next element from the current iterable, or the first element
# from the subsequent iterable--unless you’re at the end, in which case it should exit.

#Book solution:
def mychain(*args):


    for arg in args:
        for item in arg:
            yield item

    for one_item in mychain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
        print(one_item)
        