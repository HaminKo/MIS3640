def rotate_word(phrase, num):
    return_string = ''
    for i in phrase:
        if ord(i) >= 65 and ord(i) <= 90:
            if ord(i) + num > 90:
                return_string = return_string + chr(ord(i) - 26 + num)
            elif ord(i) + num < 65:
                return_string = return_string + chr(ord(i) + 26 + num)
            else:
                return_string = return_string + chr(ord(i) + num)
        elif ord(i) >= 97 and ord(i) <= 122:
            if ord(i) + num > 122:
                return_string = return_string + chr(ord(i) - 26 + num)
            elif ord(i) + num < 97:
                return_string = return_string + chr(ord(i) + 26 + num)
            else:
                return_string = return_string + chr(ord(i) + num)
        else:
            return_string = return_string + i
    return return_string


print(rotate_word('ABCDXYZ abcefgyz ^^^', -1))