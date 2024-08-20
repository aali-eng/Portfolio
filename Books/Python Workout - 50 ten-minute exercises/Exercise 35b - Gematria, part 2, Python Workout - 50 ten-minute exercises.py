# In this exercise, you’ll write two functions: gematria_for, which
# takes a single word (string) as an argument and returns the gematria
# score for that word gematria_equal_words, which takes a single word
# and returns a list of those dict words whose gematria scores match
# the current word’s score. For example, if the function is called
# with the word cat, with a gematria value of 24 (3 + 1 + 20), then
# the function will return a list of strings, all of whose gematria
# values are also 24. (This will be a long list!) Any nonlowercase
# characters in the user’s input should count 0 toward our final score
# for the word. Your source for the dict words will be the Unix file
# you used earlier in this chapter, which you can load into a list
# comprehension.

import functools
def gematria_for(string):
    score = 0
    alph = functools.reduce(lambda s, i: s + chr(i), range(97, 97 + 26), '')
    global dict
    dict = {k: v for (k, v) in zip(alph, range(1, 27))}
    for letter in string:
        if letter in dict:
            score += dict[letter]

    return score

# print(gematria_for("apple"))

def gematria_equal_words(string):
    score = gematria_for(string)

    return [one_word.strip() for one_word in open('words.txt', 'r') if gematria_for(one_word.lower()) == score]



print(gematria_equal_words("test"))


# Book solution:

# import string
#
#
# def gematria_dict():
#     return {char: index
#             for index, char
#             in enumerate(string.ascii_lowercase,
#                          1)}
#
#
# GEMATRIA = gematria_dict()
#
#
# def gematria_for(word):
#     return sum(GEMATRIA.get(one_char, 0)
#     for one_char in word)
#
#
# def gematria_equal_words(input_word):
#     our_score = gematria_for(input_word.lower())
#     return [one_word.strip()
#     for one_word in
#     open('/usr/share/dict/words')
#     if gematria_for(one_word.lower()) ==
#     our_score]
#
# print(gematria_equal_words("test"))