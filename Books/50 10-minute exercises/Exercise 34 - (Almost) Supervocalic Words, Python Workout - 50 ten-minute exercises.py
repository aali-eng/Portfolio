# In this exercise, I want you to write a get_sv function that
# returns a set of all “supervocalic” words in the dict. If you’ve
# never heard the term supervocalic before, you’re not alone: I only
# learned about such words several years ago. Simply put, such words
# contain all five vowels in English (a, e, i, o, and u), each of them
# appearing once and in alphabetical order. For the purposes of this
# exercise, I’ll loosen the definition, accepting any word that has
# all five vowels, in any order and any number of times. Your function
# should find all of the words that match this definition
# (i.e., contain a, e, i, o, and u) and return a set containing them.

def get_sv(text):
    letters = "aeiou"

    file = open(text, 'r')
    data = file.read()
    spv_words = []
    words = data.split('\n')
    for word in words:
        if all(vowel in word for vowel in letters):
            spv_words.append(word)
    print(spv_words)


get_sv('words.txt')

# Book solution:
#
# def get_sv(filename):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#
#     return {word.strip()
#     for word in open(filename)
#     if vowels < set(word.lower())}
