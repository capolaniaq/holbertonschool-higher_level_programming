#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i, name in enumerate(dir(hidden_4)):
        if name[0] != "_":
            print("{}".format(name))
