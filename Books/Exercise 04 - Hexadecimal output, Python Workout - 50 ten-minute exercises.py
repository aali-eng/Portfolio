# For this exercise, you need to write a function (hex_output)
# that takes a hex number and returns the decimal equivalent.
# That is, if the user enters 50, you’ll assume that it’s a hex
# number (equal to 0x50) and will print the value 80 to the screen.
# And no, you shouldn’t convert the number all at once using the int
# function, although it’s permissible to use int one digit at a time.

from ast import literal_eval

def hex_output(string):

    dec = literal_eval(string)

    print("The hexadecimal string is: ", string)
    print("The decimal number is: ", dec)


hex_output('0xF')

