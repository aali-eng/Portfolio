# The challenge for this exercise is to write a wordcount function
# that mimics the wc Unix command. The function will take a filename
# as input and will print four lines of output: Number of characters
# (including whitespace) Number of words (separated by whitespace)
# Number of lines Number of unique words (case sensitive, so “NO” is
# different from “no”)


def word_counter_a(file):
    text_file = open(file, 'r')
    # lines = len(text_file.readlines())

    data = text_file.read()
    chars = len(data)
    words_list = data.split()
    words = len([word for word in words_list])
    u_words = []

    for word in words_list:
        if word not in u_words:
            u_words.append(word)
            u_words_count = len(u_words)

    return chars, words, u_words_count

def word_counter_b(file):
    text_file = open(file, 'r')
    lines = len(text_file.readlines())
    return  lines

def word_counter_final(file):
    the_list = [i for i in word_counter_a(file)]
    the_list.append(word_counter_b(file))
    return the_list
print(word_counter_final('wcfile.txt'))