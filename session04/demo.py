def my_abs(number):
    if not isinstance(number, (float, int)):
        print("You didn't input a number!")
        return
    if number >= 0:
        return number
    else:
        return -number

num = int(input("Input a number: "))

my_abs(num)
my_abs(-1.4)
my_abs('t')

print(my_abs('t'))