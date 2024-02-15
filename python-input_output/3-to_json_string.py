#!/usr/bin/python3

"""
module containing a json stringification function
"""

import json


def to_json_string(obj):
    """
    converts a provided object to a JSON string
    """
    return json.dumps(obj)
