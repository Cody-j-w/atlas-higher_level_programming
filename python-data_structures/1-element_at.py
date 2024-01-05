#!/usr/bin/python3

def element_at(list, idx):
    if idx < 0 or idx >= len(list):
        return None
    else:
        return list[idx]
