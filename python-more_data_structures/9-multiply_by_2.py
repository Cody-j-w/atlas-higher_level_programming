#!/usr/bin/python3

def multiply_by_2(a_dict):
    new_dict = dict()
    for i in a_dict:
        value = a_dict[i] * 2
        new_dict.update({i: value})
    return new_dict
