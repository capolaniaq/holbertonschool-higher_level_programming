#!/usr/bin/python3
"""Module that create a class BaseGeometry"""


class BaseGeometry():
    """Function that declare Class BaseGeometry"""

    def area(self):
        """Function that raise exception of the
        public method area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that integer validator to a name and value"""

        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
        self.name = name
