# For this exercise, you’ll write a function (called ubbi_dubbi) that takes
# a single word (string) as an argument. It returns a string, the word’s
# translation into Ubbi Dubbi. So if the function is called with octopus,
# the function will return the string uboctubopubus. And if the user
# passes the argument elephant, you’ll output ubelubephubant.


def ubbi_dubbi(word):
    output = []
    word = list(word)
    for _ in word:
        if _ in "a, e, i, o, u":
            output.append("ub" + _)
        else:
            output.append(_)
    output = "".join(output)
    print(output)

word = "test"
ubbi_dubbi(word)
