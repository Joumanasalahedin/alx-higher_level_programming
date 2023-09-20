#!/usr/bin/python3
"""Module that contains class Square,
inheritance of class Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """special str method"""
        id = f"({self.id})"
        xy = f"{self.x}/{self.y}"
        size = f"{self.width}"
        return f"[Square] {id} {xy} - {size}"

    @property
    def size(self):
        """Size getter"""

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
