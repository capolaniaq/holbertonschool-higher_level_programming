#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number2 = number * -1
    last = number2 % 10
    last = last * -1
elif number >= 0:
    last = number % 10
print("Last digit of {:d} is ".format(number), end='')
if last > 5:
    print("{:d} and is greater than 5".format(last))
elif last < 6 and last != 0:
    print("{:d} and is less than 6 and not 0".format(last))
else:
    print("{:d} and is 0".format(last))
