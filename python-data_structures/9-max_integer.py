#!/usr/bin/python3

def max_integer(list=[]):
    max = 0
    if len(list) > 0:
        for i in list:
            if i > max:
                max = i
        return max
    return None
