#!/usr/bin/python3

def uniq_add(list=[]):
    new_list = []
    for i in list:
        unique = True
        for j in new_list:
            if i == j:
                unique = False
        if unique is True:
            new_list.append(i)
    sum = 0
    for i in new_list:
        sum += i
    return sum
