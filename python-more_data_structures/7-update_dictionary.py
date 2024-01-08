#!/usr/bin/python3

def update_dictionary(a_dict, key, value):
    if key in a_dict:
        a_dict[key] = value
    else:
        a_dict.update({key: value})
    return a_dict
