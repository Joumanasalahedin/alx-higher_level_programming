#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
        Args:
        width (int): width of a rectangle
        height (int): height of a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns string representation of a rectangle
        filled with character stored in print_symbol """
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle

        for _ in range(self.height):
            for _ in range(self.width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'

        return rectangle[:-1]

    def __repr__(self):
        """ Returns a string representation of the rectangle
        to recreate a new instance by using eval() """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Prints message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
