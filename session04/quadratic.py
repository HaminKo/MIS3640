# a, b, c corresponds to ax^2 + bx + c = 0
def quadratic(a, b, c):
    x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    y = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x, y

# Test using a = 1, b = 2, c=-3
print(quadratic(1, 2, -3))