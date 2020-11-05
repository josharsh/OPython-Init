"""
This example demonstrates the operator overloading example
Instructions:
- Create a class named Point
- Overload the add operator '+' to add two Point objects
- Also added is an additional function that calculates the length between 2 points
  to demonstrate the application of this exercise
"""


class Point(object):
    # the constructor
    def __init__(self, x, y):
        """
        Initialize a new data object

        Args:
            self: (todo): write your description
            x: (int): write your description
            y: (int): write your description
        """
        # these are the x, y coordinates
        self.x = x
        self.y = y

    # override the __add__ function to return a new Point class
    # with the x coordinate as the sum of the x coordinates of two points
    # and y coordinate as the sum of y coordinates of two points
    def __add__(self, other):
        """
        Return a new point to this point

        Args:
            self: (todo): write your description
            other: (todo): write your description
        """
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


# Bonus:  Find the length between two points!
def calculate_length(p1, p2):
    """
    Calculate the length of two points.

    Args:
        p1: (todo): write your description
        p2: (todo): write your description
    """
    import math
    # length = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    length = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return length


# the main entry point function
def main():
    """
    Main function.

    Args:
    """
    p1 = Point(3, 5)
    p2 = Point(-4, 10)
    p3 = p1 + p2
    print('Point p3: ({0}, {1})'.format(p3.x, p3.y))
    print('Length of the line between p1 and p2 is: {0}'.format(calculate_length(p1, p2)))


if __name__ == '__main__':
    main()
