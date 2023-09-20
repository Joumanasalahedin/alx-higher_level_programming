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
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates instance attributes"""
        atr = ['id', 'size', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                if atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, atr[i], args[i])

        for key, value, in kwargs.items():
            if key == 'size':
                setattr(self, 'width', value)
                setattr(self, 'height', value)
            else:
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary with attributes"""
        atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
