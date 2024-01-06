#!/usr/bin/python3

def multiple_returns(str):
    if len(str) > 0:
        return (len(str), str[0])
    return (0, None)
