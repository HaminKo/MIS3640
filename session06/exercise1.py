def bmi(w, h):
    bmi = 703 * w / h**2
    print(bmi)
    if bmi <=18.5:
        print('underweight')
    elif bmi <25:
        print('normal')
    elif bmi < 30:
        print('overweight')
    else:
        print('obseity')

# w = input('Give your weight in lb: ')
# h = input('Give your height in inches: ')

# bmi(int(w), int(h))

# 1.2
def varcomp(varA, varB):
    if isinstance(varA, str) or isinstance(varB, str):
        print('string involved')
        return
    if varA > varB:
        print('bigger')
    elif varA < varB:
        print('smaller')
    else:
        print('equal')
    
varA = int(input('number 1: '))
varB = int(input('number 2: '))

varcomp(varA, varB)