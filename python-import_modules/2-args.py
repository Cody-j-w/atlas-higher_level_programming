#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_count = len(argv) - 1
    if arg_count == 1:
        arg = "argument"
    else:
        arg = "arguments"
    print("{0} {1}".format(arg_count, arg), end=":\n" if arg_count != 0 else ".\n")
    for i in range(1, len(argv)):
        print("{0}: {1}".format(i, argv[i]))
