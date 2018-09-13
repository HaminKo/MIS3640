import turtle
import math
jack = turtle.Turtle()
# print(jack)

# for i in range(4):
#     jack.fd(100)
#     jack.lt(90)

# turtle.mainloop()

# Exercse 2 Problem 1 and 2
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)

# print(square(jack, 100))

# Problem 3
# def polygon(t, n, length):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)

# print(polygon(jack, 360, 1))

# Problem 4
# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, n, length)

# print(circle(jack, 50))

# #Problem 5
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * (angle/360)
#     n = int(arc_length / 3) + 1
#     for i in range(n):
#         t.fd(arc_length / n)
#         t.lt(angle / n)

# Refactoring
def polyline(t, n , length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    sub_length = arc_length / n
    sub_angle = angle / n
    polyline(t, n, sub_length, sub_angle)

def circle(t, r):
    arc(t, r, 360)

# turtle.mainloop()