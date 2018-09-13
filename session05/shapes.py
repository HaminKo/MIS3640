import turtle
import math

# Define basic shape drawing functions
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

# Additional helper functions for drawing the shapes in the exercises
def initialize_circle(t, r, x, y, angle):
    t.up()
    t.setpos(x, y)
    t.seth(angle)
    t.down()
    t.circle(r)

def set_to_mid(t, r, x, y, angle=0):
    t.up()
    t.setpos(x, y + r)
    t.down()
    t.seth(angle)

# def set_point_to_mid(t, r, x, y)

# Draws shape 1 in exercse 3
def draw_flower(t, r, petals, x=0, y=0):
    """
    Draws a circle or radius r with specified number of petals that originate from the center.
    (x, y) is the origin point for the drawing.
    """
    t.width(1)
    initialize_circle(t, r, x, y, 0)
    for i in range(petals):
        angle = 360/petals * i
        part_circle_r = r * 1/(2 * math.sin( (math.pi*2)/(2*petals) ) )
        circle_extent = 360/petals

        set_to_mid(t, r, x, y, angle)
        # Draw first half of petal
        t.circle(part_circle_r, circle_extent)
        t.lt(180 - 360/petals)
        # Finish petal
        t.circle(part_circle_r, circle_extent)

# Draws shape 2 in exercse 3
def draw_yinyang(t, r, x=0, y=0):
    """
    Draws the yinyang symbol in a circle of radius r.
    (x, y) is the origin point for the drawing.
    """
    t.width(4)
    initialize_circle(t, r, x, y, 0)
    for i in range(2):
        angle = 0 + 180 * i

        set_to_mid(t, r, x, y, angle)
        # Draw the semi circle
        t.circle(r/2, 180)
        # Draw the inner circle
        t.up()
        t.lt(90)
        t.fd(r/3)
        t.rt(90)
        t.down()
        t.circle(r/6)

# Draws shape 3 in exercise 3
def draw_circle_triangle_circle(t, r, triangles, x=0, y=0):
    """
    Draws a circle with radius r that has a specified amount of trinagles that originate from the center. Each inner triangle has a circle within it.
    (x, y) is the origin point for the drawing.
    """
    t.width(1)
    initialize_circle(t, r, x, y, 0)
    for i in range(triangles):
        angle = 360/triangles * i
        dist_to_triangle = r * math.cos(math.pi/6)
        inner_circle_r = r * 1/ (4 * math.sin(2/3 * math.pi))

        set_to_mid(t, r, x, y, angle + 60)
        # Draw the triangle
        polygon(t, 3, r)
        # Draw the inner circle
        t.up()
        t.seth(angle + 90)
        t.fd(dist_to_triangle)
        t.down()
        t.seth(angle + 180)
        t.circle(inner_circle_r)

# Draws the Archimedean spiral
# Base code from https://rosettacode.org/wiki/Archimedean_spiral
def draw_archmedean_spiral(t, a, b, degrees, x=0, y=0):
    """
    Draws and archimedean spiral with origin point at (x, y)
    """
    t.up()
    t.setpos(x, y)
    t.down()
    degrees = int(degrees/6)
    for i in range(degrees):
        t = i / 30 * math.pi
        x = (1 + 5 * t) * math.cos(t)
        y = (1 + 5 * t) * math.sin(t)
        drawer.goto(x, y)

# Initialize drawer
drawer = turtle.Turtle()
drawer.speed('fastest')

# Test functions
draw_flower(drawer, r=100, petals=6, x=-200)

draw_yinyang(drawer, r=100, x=0)

draw_circle_triangle_circle(drawer, r=100, triangles=4, x=200)

draw_archmedean_spiral(drawer, 2, 2, 360 * 5)

turtle.mainloop()