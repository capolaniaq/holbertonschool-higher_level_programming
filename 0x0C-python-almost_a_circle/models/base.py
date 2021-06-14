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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that return a JSON object as string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that write to JSON OBJECT to file"""
        list_dict = []
        file_name = cls.__name__ + '.json'
        if list_objs:
            for item in list_objs:
                list_dict += [item.to_dictionary()]
        with open(file_name, 'w', encoding='utf-8') as file_open:
            file_open.write(cls.to_json_string(list_dict))