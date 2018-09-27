

def consecutive_letter(word, times):
    consecutive_row = 0
    not_same = 0
    same = 0
    previous = word[0]
    for letter in word[1:len(word)]:
        if letter == previous and same == 0:
            consecutive_row += 1
            same += 1
            not_same = 0
        elif letter != previous and not_same == 0:
            not_same += 1
            same = 0
        elif letter != previous and not_same != 0:
            consecutive_row = 0
            not_same += 1
            same = 0
        previous = letter
        if consecutive_row == times:
            return True
    return False

print(consecutive_letter('aabbcc', 3))