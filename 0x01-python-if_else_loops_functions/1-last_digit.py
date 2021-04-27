#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number2 = number * -1
else:
    number2 = number
last = number2 % 10
print("Last digit of", end='')
if number < 0:
    lastnegative = last * -1
    if last > 5:
        print(" {:d} is {:d} and is greater than 5".format(number, lastnegative))
    elif last < 6 and last != 0:
        print(" {:d} is {:d} and less than 6 and not 0".format(number, lastnegative))
    else:
        print(" {:d} is {:d} and is 0".format(number, last))
else:
    if last > 5:
        print(" {:d} is {:d} and is greater than 5".format(number, last))
    elif last < 6 and last != 0:
        print(" {:d} is {:d} and less than 6 and not 0".format(number, last))
    else:
        print(" {:d} is {:d} and is 0".format(number, last))
