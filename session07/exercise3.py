import math

def mysqrt(a, x):
    epsilon = 0.0000001
    while True:
        # print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
        x = y

# print(mysqrt(16,5))

def test_square_root():
    print('a   mysqrt(a)     math.sqrt(a)  diff')
    print('-   ---------     ------------  ----')
    for i in range(9):
        i += 1
        a = i
        b = mysqrt(a, i)
        c = math.sqrt(a)
        d = abs(b - c)
        print('{:.1f} {:.11f} {:.11f} {:f}'.format(a,b,c,d))

test_square_root()