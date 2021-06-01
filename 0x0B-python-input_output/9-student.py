#!/usr/bin/python3
"""Module where is declare the class student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Function that declare a instance Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def first_name(self):
        """Function the Firts_name of Student"""

        return self.__first_name

    def first_name(self, value):
        """Function the Firts_name of Student"""

        if type(value) is not str:
            value = str(value)
        self.__first_name = value

    def last_name(self):
        """Function the last_name of Student"""

        return self.__last_name

    def last_name(self, value):
        """Function the last_name of Student"""

        if type(value) is not str:
            value = str(value)
        self.__last_name = value

    def age(self):
        """Function the age of Student"""
        return self.__age

    def age(self, value):
        """Function the age of Student"""
        if type(value) is not int:
            value = int(value)
        self.__age = value

    def to_json(self):
        """Function that return a dictionary of atributes
        of instance Student"""

        return self.__dict__
