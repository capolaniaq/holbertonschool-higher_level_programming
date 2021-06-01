#!/usr/bin/python3
"""Module that load data JSON form to file"""
import json


def load_from_json_file(filename):
    """Function that load data JSON of the file.json"""

    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
