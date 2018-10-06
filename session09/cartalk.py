# def consecutive_letter(word, times):
#     consecutive_row = 0
#     not_same = 0
#     same = 0
#     previous = word[0]
#     for letter in word[1:len(word)]:
#         if letter == previous:
#             if same == 0:
#                 consecutive_row += 1
#             same += 1
#             not_same = 0
#         else:
#             if not_same != 0:
#                 consecutive_row = 0
#             not_same += 1
#             same = 0
#         previous = letter
#         if consecutive_row == times:
#             return True
#     return False

def consecutive_letter(word, times):
    for i in range(1, len(word) - times * 2 + 1):
        same = 0
        for i in range(1, len(word), 2):
            if word[i] == word[i + 1]:
                print('called')
                same += 1
            if same == times:
                return True
    return False

print(consecutive_letter('abbccdd', 3))

def age_switch():
    mom = 0
    son = 0
    for i in range(1, 100):
        printstring = ''
        mom = i
        son = 0
        for j in range(1, 100):
            momstr = str(mom)
            sonstr = str(son)
            if len(sonstr) == 1:
                sonstr = '0' + sonstr
            if momstr[0] == sonstr[1] and momstr[1] == sonstr[0]:
                printstring = printstring + str(mom) + ' ' + str(son) + ' | '
            mom += 1
            son += 1
        if len(printstring) > 0:
            print(printstring)

# age_switch()