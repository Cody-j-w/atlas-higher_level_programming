#!/usr/bin/python3

def best_score(a_dict):
    if len(a_dict) == 0:
        return None
    for i in a_dict:
        if type(a_dict[i]) is str:
            a_dict[i] = int(a_dict[i])
    return max(a_dict, key=a_dict.get)

my_dict = {'a': "6", 'b': -2, 'c': -1, 'd': -46}
print(best_score(my_dict))

