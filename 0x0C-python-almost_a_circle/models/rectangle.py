#!/usr/bin/python3
"""Module that contains class Rectangle,
inheritance of class Base"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints Rectange instance with the '#' character"""
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle

        rectangle += '\n' * self.y

        for _ in range(self.height):
            for _ in range(self.x):
                rectangle += ' '
            for _ in range(self.width):
                rectangle += '#'
            rectangle += '\n'

        print(rectangle[:-1])

    def __str__(self):
        """str special method"""
        id = f"({self.id})"
        xy = f"{self.x}/{self.y}"
        wh = f"{self.width}/{self.height}"
        return f"[Rectangle] {id} {xy} - {wh}"

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        atr = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, atr[i], args[i])

        for key, value, in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary with attributes"""
        atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in atr:
            dict_res[key] = getattr(self, key)

        return dict_res
