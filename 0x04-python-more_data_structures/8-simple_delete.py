#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dictionary = a_dictionary
    if key in a_dictionary:
        new_dictionary = new_dictionary.pop(key)
    return new_dictionary
