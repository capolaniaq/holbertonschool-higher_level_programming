#!/usr/bin/python3
def no_c(my_string):
    count = 0
    for i, letter in enumerate(my_string):
        if letter == 'C' or letter == 'c':
            if i == 0:
                my_string = my_string[1:]
                count = count + 1
            elif i > 0:
                my_string = my_string[:i - count] + my_string[i + 1 - count:]
                count = count + 1
    return my_string
