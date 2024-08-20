# In many cases, we want to take a file in one format and
# save it to another format. In this function, we do a basic
# version of this idea. The function takes two arguments:
# the names of the input file (to be read from) and
# the output file (which will be created). For example, if
# a file looks like
# abc def
# ghi jkl
#
# then the output file will be
# fed cba
# lkj ihg
#
# Notice that the newline remains at the end of the string, while
# the rest of the characters are all reversed.

def reverse_file(input_file, output_file):
    file = open(input_file, 'r')
    data = file.read()
    reversed_data = data[::-1]
    file_path = output_file + ".txt"
    with open(file_path, 'w') as file:
        file.write(reversed_data)
        print("The data has been reversed and saved.")


reverse_file('wcfile.txt', 'wcfile_reversed.txt')


#Book solution:
# def reverse_lines(infilename, outfilename):
#     with open(infilename) as infile, open(outfilename, 'w') as outfile:
#         for one_line in infile:
#             outfile.write(f'{one_line.rstrip()[::-1]}\n')
