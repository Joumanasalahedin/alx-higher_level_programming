#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
        Args:
        width (int): width of a rectangle
        height (int): height of a rectangle
        """
        self.width = width
        self.height = height

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
