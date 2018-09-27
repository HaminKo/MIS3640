# Exercise 1

def more_than_20(word):
    if len(word) > 20:
        print(word)

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def avoids(word, letters):
    for letter in word:
        if letter in letters:
            return False
    return True

def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

# def uses_all(word, letters):
#     for letter in letters:
#         if letter not in word:
#             return False
#     return True

def uses_all(word, letters):
    return uses_only(letters, word)

# def is_abecedarian(word):
#     compare = 0
#     for letter in word:
#         if ord(letter) < compare:
#             return False
#         compare = ord(letter)
#     return True

def is_abecedarian(word):
    previous = word[0]
    for letter in word:
        if letter < previous:
            return False
        previous = letter
    return True

# Exercise 2

# Recursion
def is_abedecarian1(word):
    n = len(word)
    if n == 1:
        return True
    elif word[n-2] > word[n-1]:
        return False
    else:
        return is_abedecarian1(word[0:n-1])

# While
def is_abedecarian2(word):
    counter = 0
    while counter < len(word) - 1:
        previous = word[counter]
        counter += 1
        if word[counter] < previous:
            return False
    return True

print(is_abedecarian2('abcb'))