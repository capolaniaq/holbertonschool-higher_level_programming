#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} Arguments.".format(0))
    elif len(sys.argv) == 2:
        print("{} Argument:".format(len(sys.argv) - 1))
    else:
        print("{} Arguments:".format(len(sys.argv) - 1))
    for i, argv in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, argv))
