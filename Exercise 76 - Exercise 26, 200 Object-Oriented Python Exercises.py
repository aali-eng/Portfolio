# Create a class PhoneBook with the functions insert(), delete() and lookup()

class PhoneBook:
    def insert(self, name, number):
        self.name = name
        self.number = number

    def delete(self, name_to_remove):
        self.name_to_remove = name_to_remove
        if name_to_remove == self.name:
            del self.name
            print(f"{name_to_remove} was removed from PhoneBook.")
            pass

    def lookup(self, input_name):
        self.input_name = input_name
        try:
            if input_name == self.name:
                print(f'Name: {self.name}, number: {self.number}')
        except:
            print("There is no account by such name.")

name = PhoneBook()
name.insert("John", "1234")
name.lookup("John")
name.delete("John")
name.lookup("John")


# Book solution:

class PhoneBook:
     db = {}
     def insert(self, name, number):
         self.db[name] = number

     def delete(self, name, number):
         del self.db[name]

     def lookup(self, name):
         print(self.db[name])

mybook = PhoneBook()
mybook.insert("Acme", "101-123-456")
mybook.insert("Foo", "166-689-452")

mybook.lookup("Acme")
