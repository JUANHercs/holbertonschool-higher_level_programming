#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv) - 1
    if x == 0:
        print("{} argument.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
        print("{}: {}".format(x, sys.argv[x]))
    else:
        print("{} arguments:".format(x))
        for i in range(1, x + 1):
            print("{}: {}".format(i, sys.argv[i]))
