# fin = open("words.txt")
# line = (fin.readline())
# line = (fin.readline())
# print(line)

def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    if len(word) > 20:
        print(word)


# read_long_words()

def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    # for letter in word:
    #     if letter.lower() == 'e':
    #         return False
    # return True
    return not 'e' in word.lower()



# print(has_no_e('Babson'))
# print(has_no_e('College'))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True


# print(avoids('Babson', 'ab'))
# print(avoids('College', 'ab'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    return uses_only(required, word)


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    previous = word[0]
    for letter in word:
        if letter < previous:
            return False
        previous = letter
    return True


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

def use_function(data, thefunc, condition):
    counter = 0
    compare = 0
    for line in data:
        counter += 1
        word = line.strip()
        if thefunc(word, condition) == True:
            compare += 1
    print(compare)
    print(compare/counter)

fin = open("words.txt")
print(use_function(fin, uses_all, 'abc'))