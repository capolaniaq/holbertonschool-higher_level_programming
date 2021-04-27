#!/usr/bin/python3
for i in range(0, 100):
    first = i / 10
    last = i % 10
    if first != last:
        if i % 10 == 0:
            first = first + 1
        elif first >= last:
            first = first + 1
        elif i != 89:
            print("{:02d}, ".format(i), end="")
        else:
            print("{:02d}".format(i))
