import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)


# print(distance_between_points(john, my_point))



class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """



def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p


def find_corners(rect):
    """ Returns an array of points for corners of a Rectangles

    rect: Rectangle
    returns: array of points were the corners in the rectangle are: [bottom left, bottom right, top left, top right]
    """

    bl = Point()
    br = Point()
    tl = Point()
    tr = Point()

    bl.x = rect.corner.x
    bl.y = rect.corner.y
    br.x = rect.corner.x + rect.width
    br.y = rect.corner.y
    tl.x = rect.corner.x
    tl.y = rect.corner.y + rect.height
    tr.x = rect.corner.x + rect.width
    tr.y = rect.corner.y + rect.height
    return [bl, br, tl, tr]

def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight




def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)


class Circle:
    """
    Represents a circle.

    Attributes: center, radius
    """

def point_in_circle(circle, point):
    """
    Returns True if the point lies in the circle.
    circle: Circle object
    point: Point object

    returns: boolean
    """
    return distance_between_points(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    """
    Returns True if the entire rectangle lies in the circle.
    circle: Circle object
    rect: Rectangle object

    returns: boolean
    """
    corners = find_corners(rect)
    for corner in corners:
        if not point_in_circle(circle.center, corner):
            return False
    return True

def rect_circle_overlap(circle, rect):
    """
    Returns True if any corner of the rectangle lies in the circle.
    circle: Circle object
    rect: Rectangle object

    returns: boolean
    """
    corners = find_corners(rect)
    for corner in corners:
        if point_in_circle(circle.center, corner):
            return True,
    return False

def rect_circle_overlap_2(circle,rect):
    """
    Returns true if any part of the rectangle lies in the circle.
    circle: Circle object
    rect: Rectangle object

    returns: boolean
    """
    if rect_circle_overlap(circle, rect):
        return True
    corners = find_corners(rect)
    if corners[0].x <= circle.center.x and corners[1].x >= circle.center.x:
        if circle.center.y + circle.radius >= corners[0].y and circle.center.y - circle.radius.y <= corners[0].y:
            return True
        if circle.center.y + circle.radius >= corners[2].y and circle.center.y - circle.radius.y <= corners[2].y:
            return True
    elif corners[0].y <= circle.center.y and corners[2].y >= circle.center.y:
        if circle.center.x + circle.radius >= corners[0].x and circle.center.x - circle.radius.x <= corners[0].x:
            return True
        if circle.center.x + circle.radius >= corners[1].x and circle.center.x - circle.radius.x <= corners[1].x:
            return True
    return False


def main():
    # my_point = Point()
    # print(Point.__doc__)
    # my_point.x = 3
    # my_point.y = 4
    # print('My point', end=' ')
    # print_point(my_point)

    # print('Is my_point an instance of Point?', isinstance(my_point, Point))
    # print('Is my_point an instance of Rectangle?',
    #       isinstance(my_point, Rectangle))
    # print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    # print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    # box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 0.0
    # box.corner.y = 0.0

    # print('Does box have an attribute x?', hasattr(box, 'x'))

    # print('Does box have an attribute corner?', hasattr(box, 'corner'))

    # print('Rectangle has these:', dir(box))

    # center = find_center(box)
    # print('center', end=' ')
    # print_point(center)

    # print(box.width)
    # print(box.height)
    # print('grow')
    # grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)

    example_circle = Circle()
    circle_center = Point()
    circle_center.x = 150
    circle_center.y = 100
    example_circle.center = circle_center
    example_circle.radius = 75



if __name__ == '__main__':
    main()
