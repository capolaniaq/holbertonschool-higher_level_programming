#!/usr/bin/python3
"""Module that created a Class Base"""

import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Function that return a JSON object as string"""
        return json.dumps(list_dictionaries)
