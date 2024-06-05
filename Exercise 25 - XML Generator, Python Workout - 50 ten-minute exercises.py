# Write a function, myxml, that allows you to create simple XML output.
# The output from the function will always be a string. The function can
# be invoked in a number of ways, as shown in table 6.3.
#
#
# myxml('foo') <foo></foo>
# myxml('foo', 'bar') <foo>bar</foo>
# myxml('foo', 'bar', a=1, b=2, c=3) <foo a="1" b="2" c="3">bar</foo>
#
# Notice that in all cases, the first argument is the name of the tag.
# In the latter two cases, the second argument is the content (text)
# placed between the opening and closing tags. And in the third case,
# the name-value pairs will be turned into attributes inside of the opening tag.

def myxml(arg, content='', **kwargs):
    attr = ''.join([f'{key}="{value}"' for key, value in kwargs.items()])
    output = f"<{arg} {attr}>{content}</{arg}>"
    return output

print(myxml('tagname', 'hello', a=1, b=2, c=3))
