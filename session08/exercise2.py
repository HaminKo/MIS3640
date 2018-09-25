
# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def counter(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    return count

# print(counter("a", "New England Patriots"))