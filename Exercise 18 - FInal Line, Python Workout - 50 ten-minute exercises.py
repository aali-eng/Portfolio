# In this exercise, write a function (get_final_line) that takes a filename
# as an argument. The function should return that file’s final line on the screen.

def get_final_line(file):
    final_line = file.readlines()[-1]
    print(final_line)

# Book solution:
# def get_final_line(filename):
#     final_line = ''
#     for current_line in open(filename):
#     final_line = current_line
#
#
# return final_line
#
# print(get_final_line('/etc/passwd'))
