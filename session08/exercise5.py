def any_lowercase1(s):
    '''
    Return true if the first letter is lowercase, false otherwise.
    '''
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):
    '''
    Returns true.
    '''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    '''
    Returns true if the last letter is lowercase, false otherwise.
    '''
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    '''
    Returns true if any letter is lowercase, false otherwise.
    '''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    '''
    Returns true if all letters are lowercase, false otherwise.
    '''
    for c in s:
        if not c.islower():
            return False
    return True
