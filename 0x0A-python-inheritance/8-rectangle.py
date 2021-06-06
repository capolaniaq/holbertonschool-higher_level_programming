#!/usr/bin/python3
"""Module that declare rectangle(BaseGeometry)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle inherits Basegeometry"""

    def __init__(self, width, height):
        self.__height = height
        self.__width = width
