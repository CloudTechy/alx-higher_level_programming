#!/usr/bin/python3

""" module that creates a list from args and save as json file. """


import sys
if __name__ == "__main__":
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file

    try:
        args = load("add_item.json")
    except FileNotFoundError:
        args = []
    args.append(sys.argv[1:])
    save(args, filename="add_item.json")
