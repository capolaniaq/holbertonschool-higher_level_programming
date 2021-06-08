#!/usr/bin/python3
"""Module that created a Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantions"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x"""
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y"""
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """test return the area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """function that print the  rectangle with #
        character"""
        for row in range(self.height):
            for column in range(self.width):
                print("#", end="")
            print()
