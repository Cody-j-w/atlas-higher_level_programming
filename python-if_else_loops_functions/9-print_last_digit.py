#!/usr/bin/python3

def print_last_digit(number):
    numMod = abs(number) % 10
    print("{}".format(numMod), end="")
    return numMod
