#!/usr/bin/python3

def divisible_by_2(list=[]):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
