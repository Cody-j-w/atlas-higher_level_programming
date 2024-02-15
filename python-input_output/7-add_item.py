#!/usr/bin/python3

"""
this module saves and loads entries to and from a JSON file.
New entries are passed as arguments to the script, and saved
to a list saved as JSON using the save_to_json_file and load_from_json_file
functions
"""
import sys
from os.path import isfile
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if isfile('./add_item.json'):
    object_list = load('./add_item.json')
else:
    object_list = []
for i in range(1, len(sys.argv)):
    object_list.append(sys.argv[i])
save(object_list, 'add_item.json')
