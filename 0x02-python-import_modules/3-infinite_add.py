#!/usr/bin/python3
import sys
if __name__ == "__main__":
    add = 0
    for i, integer in enumerate(sys.argv):
        if i > 0:
            add = add + int(integer)
    print("{}".format(add))
