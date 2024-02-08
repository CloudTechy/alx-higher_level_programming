#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for x in my_string:
        if my_string[x] == 'c' or my_string[x] == 'C':
            continue
        new_string += my_string[x]
