#!/usr/bin/python3
"""Module that create a class MyList inherits from list
"""


class MyList(list):
    """MyList inherits to List"""

    def __init__(self):
        """Function that stored the lits items"""

        self.list = list

    def print_sorted(self):
        """Function that print the contain of lisr in sort"""

        sort_list = []
        for i in sorted(self):
            sort_list.append(i)
        print(sort_list)
