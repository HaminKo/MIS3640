exvar = 1

def exfunc(a):
    print(a, "a")
    a = 10
    print(a, "b'")
    print("this workjs!")
    return a

def exfunc2(a=0, b=0):
    if exvar > 9:
        print("oops")
    else:
        print("1")

print(exvar)
exfunc(exvar)
print(exvar)
exfunc2()

