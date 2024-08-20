# Write a function, most_repeating_word, that takes a sequence of strings
# as input. The function should return the string that contains the greatest
# number of repeated letters. In other words For each word, find the letter
# that appears the most times. Find the word whose most-repeated letter appears
# more than any other.


# from collections import Counter
#
# def most_repeating_word(string):
#     word_list = string.split()
#     counting2 = []
#     for word in word_list:
#         counting = Counter(word).most_common(1)
#         counting1 = [word, counting[0][1]]
#
#
#         print(counting1)
#
#
#
# most_repeating_word("bbb This is testtt")

from collections import Counter
import operator

WORDS = ['this', 'is', 'an',
         'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)


print(most_repeating_word(WORDS))
