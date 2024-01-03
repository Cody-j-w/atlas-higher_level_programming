#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        numMod = -(abs(number) % 10)
    else:
        numMod = abs(number) % 10
    print("{}".format(numMod), end="")
    return numMod
