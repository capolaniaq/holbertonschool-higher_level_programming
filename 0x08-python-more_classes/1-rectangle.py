#!/usr/bin/python3
"""Module of define a empty class Rectangle"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Function to validade of the width and height of rectangle"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Function that validade fo the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Function that validade fo the height"""
        if type(value) is not int:
            print("width must be an integer", end="")
            raise TypeError
        if value < 0:
            print("width must be >= 0", end="")
            raise ValueError
        self.__height = value

    @property
    def width(self):
        """Function that validade fo the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Function that validade fo the width"""
        if type(value) is not int:
            print("width must be an integer", end="")
            raise TypeError
        if value < 0:
            print("width must be >= 0", end="")
            raise ValueError
        self.__width = value
