#!/usr/bin/python3

"""
module containing function to write content to a file, overwriting as needed
"""
import json


def save_to_json_file(object, filename):
    """
    Save content to a file as a JSON object

    Args:
        filename: the name of the file.
        object: the content being saved as JSON
    """

    with open(filename, 'w') as file:
        file.write(json.dumps(object))
