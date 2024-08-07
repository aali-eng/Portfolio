# Can you create objects in a loop?

"""
Yes:
"""
test = []
for i in range(0,50):
    obj = TestClass()
    test.append(obj)
