#!/usr/bin/python3
import json
from sys import argv
import os
save_json_file = __import__('5-save_to_json_file').save_to_json_file
load_json_file = __import__('6-load_from_json_file').load_from_json_file

items = []
if os.path.exists("add_item.json"):
    items = load_json_file("add_item.json")

for arg in argv[1:]:
    items.append(arg)

save_json_file(items, "add_item.json")
