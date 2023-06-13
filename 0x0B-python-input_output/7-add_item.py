#!/usr/bin/python3
"""Defines a function that adds all arguments from a list into a file"""


import sys

if __name__ = "__main__"
save_to_json_file = __import__(5-save_to_json_file.py).save_to_json_file
load_from_json_file = __import__(6-load_from_json_file.py).load_from_json_file
args = sys.argv

if not os.path.exists("add_item.json"):
    with open("add_item.json", "w", encoding="utf") as f:
        f.write("[]")

obj = load_from_json_file("add_item.json")

for arg in args[1:]:
    obj.append(arg)

save_to_json_file(obj, "add_item.json")
