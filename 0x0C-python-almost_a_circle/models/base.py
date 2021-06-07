#!/usr/bin/python3
"""Module that created a Class Base"""


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
