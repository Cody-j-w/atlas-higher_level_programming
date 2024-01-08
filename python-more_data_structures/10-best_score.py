#!/usr/bin/python3

def best_score(a_dict):
    max = -1000000000
    for i in a_dict:
        if a_dict[i] > max:
            max = a_dict[i]
    if max == -1000000000:
        return None
    return max
