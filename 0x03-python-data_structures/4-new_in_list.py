#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i, number in enumerate(my_list):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(number)
    return new_list
