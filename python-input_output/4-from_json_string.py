#!/usr/bin/python3

"""
module containing a json de-stringification function
"""

import json


def from_json_string(obj):
    """
    converts a provided object from a JSON string
    """
    return json.loads(obj)
