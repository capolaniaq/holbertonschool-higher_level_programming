#!/usr/bin/python3
def safe_print_list_integers(value=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(value[i]), end="")
            count = count + 1
        except TypeError:
            pass
        except ValueError:
            pass
        except IndexError:
            raise
    print("")
    return count
