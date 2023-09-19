#!/usr/bin/python3
"""Module with class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the printable string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
