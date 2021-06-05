#!/usr/bin/python3
"""Module that check  object is an instance of a
class that inherited (directly or indirectly)
from the specified class """


def inherits_from(obj, a_class):
    """Function  object is an instance of a
    class that inherited (directly or indirectly) from the
     specified class"""

    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False
