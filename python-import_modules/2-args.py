#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 1:
        arg = "argument"
    else:
        arg = "arguments"
    print("{0} {1}".format(argc, arg), end=":\n" if argc != 0 else ".\n")
    for i in range(1, len(argv)):
        print("{0}: {1}".format(i, argv[i]))
