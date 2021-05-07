#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, row in enumerate(matrix):
        for x, number in enumerate(row):
            print("{:d}".format(number), end="")
            if x < len(row) - 1:
                print(end=" ")
        print()
