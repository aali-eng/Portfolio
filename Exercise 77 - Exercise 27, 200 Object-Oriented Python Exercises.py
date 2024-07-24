# Create a class AddressBook with the functions add() and lookup()

class AddressBook:
    db = []

    def add(self, address):
        self.address = address
        self.db.append(address)

    def lookup(self, text):
        if text in self.address:
            print(self.address)

book1 = AddressBook()
book1.add("Lesi Ukrainki st., Kyiv")
book1.lookup("Lesi")
