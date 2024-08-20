# In this exercise, I want you to write a function that takes
# a filename as an argument. It returns a string with the file’s
# contents, but with each word translated into Pig Latin, as per
# our plword function in chapter 2 on “strings.” The returned
# translation can ignore newlines and isn’t required to handle
# capitalization and punctuation in any specific way.



def plfiletranslator(file):
    with open(file, 'r') as f:
        data = f.read()
        words_list = data.split()
        new_words_list = []
        for word in words_list:
            if word[0] in "a, e, i, o, u":
                word = word.lower()
                word += "way"
                new_words_list.append(word)
            else:
                word = word.lower()
                word = word[1:] + word[0] + "ay"
                new_words_list.append(word)
        print(new_words_list)


plfiletranslator('wcfile.txt')


# Book solution:
#
# def plword(word):
#     if word[0] in 'aeiou':
#         return word + 'way'
#
#     return word[1:] + word[0] + 'ay'
#
#
# def plfile(filename):
#     return ' '.join(plword(one_word)
#                     for one_line in open(filename)
#     for one_word in one_line.split())


