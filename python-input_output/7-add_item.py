#!/usr/bin/python3
import sys
from os.path import isfile

"""
this module saves and loads entries to and from a JSON file
"""

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if isfile('./add_item.json'):
    object_list = load('./add_item.json')
else:
    object_list = []
for i in range(1, len(sys.argv)):
    object_list.append(sys.argv[i])
save(object_list, 'add_item.json')
