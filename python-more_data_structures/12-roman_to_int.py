#!/usr/bin/python3

def roman_to_int(s):
    r_v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    if s is None:
        return res
    if type(s) is str:
        for i in range(len(s)):
            if i > 0 and r_v[s[i]] > r_v[s[i - 1]]:
                res += r_v[s[i]] - 2 * r_v[s[i - 1]]
                i += 2
            else:
                res += r_v[s[i]]
                i += 1
    return res
