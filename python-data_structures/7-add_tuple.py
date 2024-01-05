#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    proto_tuple = [0, 0]
    for i in range(2):
        if len(tuple_a) > i:
            proto_tuple[i] += tuple_a[i]
        if len(tuple_b) > i:
            proto_tuple[i] += tuple_b[i]
    tuple_c = (proto_tuple[0], proto_tuple[1])
    return tuple_c

tuple_a = (12, 52)
tuple_b = (46,)
print("{}".format(add_tuple(tuple_a, tuple_b)))
