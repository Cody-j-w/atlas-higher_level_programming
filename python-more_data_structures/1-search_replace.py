#!/usr/bin/python3

def search_replace(list, search, replace):
    new_list = []
    for i in list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
