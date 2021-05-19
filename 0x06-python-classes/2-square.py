#!/usr/bin/python3
"""Module that declare class Square with a private instance attribute size:"""


class Square:
    """class Square with a private attrivute size"""
    def __init__(self, size=0):
        """Function to validade of the size square"""
        self.__size = size
        try:
            if size < 0:
                raise ValueError ("size must be >= 0")
        except TypeError:
            raise TypeError ("size must be an integer")
