#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    if my_list is None:
        return idx
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            idx += 1
        except (TypeError, ValueError):
            pass
        except (IndexError):
            print("")
            return idx
    print("")
    return idx


