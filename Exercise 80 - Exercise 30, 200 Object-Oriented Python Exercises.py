# Finish the code below
#
# class PasswordManager:
#     def __init__(self):
#         pass
#
# pm = PasswordManager()
# pm.add("twitter.com","frank","password")



class PasswordManager:
    db = {}
    def __init__(self):
        pass

    def add(self, website, name, password):
        self.db[website] = name, password

pm = PasswordManager()
pm.add("twitter.com", "frank", "password")

print(pm.db)


# Book solution:

class PasswordManager:
    db = {}
    def __init__(self):
        pass

    def add(self, website, username, password):
        self.db[website] = (username, password)

pm = PasswordManager()
pm.add("twitter.com","frank","password")

print(pm.db["twitter.com"])



