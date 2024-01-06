#!/usr/bin/python3

def delete_at(list=[], idx=0):
    if idx < 0 or idx > len(list) - 1 or len(list) == 0:
        return list
    del list[idx]
    return list
