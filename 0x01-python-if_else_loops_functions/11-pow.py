#!/usr/bin/python3
def pow(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    if b < 0:
        b1 = b * -1
    else:
        b1 = b
    power = 1
    for index in range(0, b1):
        power = power * a
    if b < 0:
        return 1/power
    else:
        return power
