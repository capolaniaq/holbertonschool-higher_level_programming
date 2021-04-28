#!/usr/bin/python3
def uppercase(str):
    for index in range(len(str)):
        letter = ord(str[index])
        if 97 <= letter <= 122:
            letter = letter - 32
        else:
            letter = letter
        print("{}".format(chr(letter)), end='')
    print()
