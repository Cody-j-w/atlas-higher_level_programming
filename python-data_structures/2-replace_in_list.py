#!/usr/bin/python3

def replace_in_list(list, idx, ele):
    if idx < 0 or idx >= len(list):
        return list
    else:
        list[idx] = ele
        return list
