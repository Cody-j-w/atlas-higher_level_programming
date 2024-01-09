#!/usr/bin/python3

def roman_to_int(str):
    r_v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(str)):
        if i > 0 and r_v[str[i]] > r_v[str[i - 1]]:
            res += r_v[str[i]] - 2 * r_v[str[i - 1]]
            i += 2
        else:
            res += r_v[str[i]]
            i += 1
    return res
