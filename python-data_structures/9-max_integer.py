#!/usr/bin/python3

def max_integer(list=[]):
    if len(list) > 0:
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max
    return None
