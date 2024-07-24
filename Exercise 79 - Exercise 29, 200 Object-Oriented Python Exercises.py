# Create a class Magazine with title and pages. Then create two objects
# (magazines) with a different title and page content
#
class Magazine:

    def title(self, title):
        self.title = title

    def pages(self, pages):
        self.pages = pages


magazine = Magazine()
magazine.title("Test")
magazine.pages("Test text")

magazine2 = Magazine()
magazine2.title("Test 2")
magazine2.pages("Test text 2")

print(magazine.__dict__)
print(magazine2.__dict__)

# Book solution:

class Magazine:
    title = ""
    pages = []

diy = Magazine()
diy.title = "DIY magazine January"
diy.pages.append("Page 1: text text text")
diy.pages.append("Page 2: text text text")

cooking = Magazine()
cooking.title = "Excellent cuisine"
cooking.pages.append("Page 1: text text text")
cooking.pages.append("Page 2: text text text")
