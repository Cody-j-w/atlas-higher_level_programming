#!/usr/bin/python3

def new_in_list(list, idx, element):
    new_list = []
    for i in range(len(list)):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(list[i])
    return new_list
