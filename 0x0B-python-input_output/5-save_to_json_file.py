#!/usr/bin/python3
"""Module that write JSON object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Function that write to JSON OBJECT to file"""

    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
