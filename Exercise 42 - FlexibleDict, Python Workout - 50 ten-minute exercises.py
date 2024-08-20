# In this exercise, we’ll also implement a subclass of dict,
# which I call FlexibleDict. Dict keys are Python objects,
# and as such are identified with a type. So if you use key
# 1 (an integer) to store a value, then you can’t use key '1'
# (a string) to retrieve that value. But FlexibleDict will
# allow for this. If it doesn’t find the user’s key, it will
# try to convert the key to both str and int before giving
# up; for example
#
# fd = FlexibleDict()
#
# fd['a'] = 100
# print(fd['a'])
#
# fd[5] = 500
# print(fd[5])
#
# fd[1] = 100
# print(fd['1'])
#
# fd['1'] = 100
# print(fd[1])

# Book solution:

class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)


fd = FlexibleDict()

fd['a'] = 100
print(fd['a'])

fd[5] = 500
print(fd[5])

fd[1] = 100
print(fd['1'])

fd['1'] = 100
print(fd[1])


