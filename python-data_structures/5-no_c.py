#!/usr/bin/python3

def no_c(str):
    new_str = ""
    for i in range(len(str)):
        if str[i] != "c" and str[i] != "C":
            new_str += str[i]
    return new_str
