# What’s wrong with the code below?
#
# class Notepad:
#     def new():
#          self.document = ""
#
#
# window = Notepad()
# window.new()


"""
"Self" and " documennt" are absent from the function's parentheses,
"self.document" should initialize to "document", "window.new()" shouldn't be absent.
"""

# Book solution:

def new(self):
