#!/usr/bin/python3
"""Module of define a empty class Rectangle"""


class Rectangle:
    """Class Rectangle"""

    number_of_instances = 0
    """variable of the count instances"""

    def __init__(self, width=0, height=0):
        """Function to validade of the width and height of rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Function that validade fo the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Function that validade fo the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Function that validade fo the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Function that validade fo the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that return area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Function that return perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """Function that return representation of the rectangle with #"""
        Rectangleprint = ""
        if self.height == 0 or self.width == 0:
            return Rectangleprint
        for h in range(0, self.height):
            for w in range(0, self.width):
                Rectangleprint += "#"
            Rectangleprint += "\n"
        return Rectangleprint[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Function that delete a instance object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
