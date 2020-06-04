#!/usr/bin/python3


import sys
import os.path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


arg = sys.argv[1:]
read_list = []

if os.path.isfile("add_item.json"):
    read_list = load_from_json_file("add_item.json")
    read_list += arg
save_to_json_file(read_list, "add_item.json")
