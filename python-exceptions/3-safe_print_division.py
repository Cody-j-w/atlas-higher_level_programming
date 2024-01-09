#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except:
        result = None
    finally:
        try:
            print("Inside result: {:d}".format(result))
            return result
        except:
            print("Inside result: {}".format(result))
            return result
