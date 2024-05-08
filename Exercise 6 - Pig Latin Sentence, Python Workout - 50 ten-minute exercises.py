# Now that you’ve successfully written a translator for a single English word,
# let’s make things more difficult: translate a series of English words into
# Pig Latin. Write a function called pl_sentence that takes a string containing
# several words, separated by spaces. (To make things easier, we won’t actually
# ask for a real sentence. More specifically, there will be no capital letters
# or punctuation.)


def pl_sentence(string):
    words_list = string.split()
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

text = "This is text"
pl_sentence(text)