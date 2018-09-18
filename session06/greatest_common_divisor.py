def gcd(x, y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

num1 = int(input("give the first number: "))
num2 = int(input("give the second number: "))

print(gcd(num1, num2))