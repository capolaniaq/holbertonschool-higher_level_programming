#!/usr/bin/python3
"""
Module that contain the fucntion add_integer
"""


def matrix_divided(matrix, div):
    """
    function that divide all characters of the list of
    list with integers/floats
    Return the result in datatype
    Raise typeError matrix must be a matrix
    (list of lists) of integers/floats;
    Each row of the matrix must have the same size;
    div must be a number
    Raise ZeroDivisionError division by zero
    """
    new_matrix = []
    new_row = []
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of \
integers/floats"
            )
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of \
integers/floats"
            )
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if len(matrix[i]) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of \
integers/floats"
            )
        for x in matrix[i]:
            if type(x) is not int and type(x) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
integers/floats"
                )
            elif x is None:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
integers/floats"
                )
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of \
integers/floats"
            )
    for i, row in enumerate(matrix):
        for x, number in enumerate(row):
            new_row.append(round((number / div), 2))
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
