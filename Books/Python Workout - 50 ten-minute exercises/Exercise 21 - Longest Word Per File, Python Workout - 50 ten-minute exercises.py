# In this exercise, write two functions. find_longest_word takes
# a filename as an argument and returns the longest word found in
# the file. The second function, find_all_longest_words, takes
# a directory name and returns a dict in which the keys are filenames
# and the values are the longest words from each file.
import os

def find_longest_word(file):
    text_file = open(file, 'r')

    reading_file = text_file.read()

    data = reading_file.split()

    lengths = [len(s) for s in data]

    longest_index = lengths.index(max(lengths))

    longest_string = data[longest_index]

    print(longest_string)

find_longest_word('wcfile.txt')


def find_all_longest_words(dirname):
    return {filename: find_longest_word(os.path.join(dirname, filename))
    for filename in os.listdir(dirname)
    if os.path.isfile(os.path.join(dirname, filename))}


print(find_all_longest_words('.'))
