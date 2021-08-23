#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""

    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    peak = 0
    for number in list_of_integers:
        if number > peak:
            peak = number
    return peak
