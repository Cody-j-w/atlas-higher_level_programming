#!/usr/bin/python3

def print_sorted_dictionary(a_dict):
    keys = list(a_dict.keys())
    keys.sort()
    for i in keys:
        print("{}: {}".format(i, a_dict[i]))
