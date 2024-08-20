# For this exercise, create a function, passwd_to_csv, that takes two filenames
# as arguments: the first is a passwd-style file to read from, and the second
# is the name of a file in which to write the output. The new file’s contents
# are the username (index 0) and the user ID (index 2). Note that a record may
# contain a comment, in which case it will not have anything at index 2; you
# should take that into consideration when writing the file. The output file
# should use TAB characters to separate the elements.

# Book Solution:
import csv


def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd,
         open(csv_filename, 'w') as output:
    infile = csv.reader(passwd,
                        delimiter=':')
    outfile = csv.writer(output,
                         delimiter='\t')
    for record in infile:
        if len(record) > 1:
            outfile.writerow((record[0], record[2]))

