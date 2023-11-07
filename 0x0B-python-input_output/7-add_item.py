#!/usr/bin/python3
'''
a script to save a file to JSON
'''
import sys
import json
from os import path


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if path.exists("add_item.json"):
    mylist = load_from_json_file("add_item.json")
else:
    mylist = []

for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])

save_to_json_file(mylist, "add_item.json")
