#!/usr/bin/python3

def best_score(a_dict):
    if len(a_dict) == 0 or a_dict is None:
        return None
    return max(a_dict, key=a_dict.get)

