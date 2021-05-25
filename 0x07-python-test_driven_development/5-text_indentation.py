#!/usr/bin/python3
"""
Module that contain the fucntion text_indentation
"""


def text_indentation(text):
    """Function that print skin line after [., ?, :] characters
    a new line don't beginning fot a space
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    counter = 0
    for i, character in enumerate(text):
        if character in ['.', '?', ':']:
            print("{}".format(character))
            print()
            counter = 1
        elif text[i] in [" ", "\t"] and counter == 1:
            pass
        else:
            print("{}".format(character), end="")
            counter = 0
