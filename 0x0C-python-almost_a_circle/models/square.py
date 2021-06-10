#!/usr/bin/python3
"""Module that created a Class Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """instations Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Function that return a str to print"""
        return ("[Square] ({}) {}/{} - \
{}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Function property of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Fucntion setter that size"""
        self.width = value
        self.height = value
