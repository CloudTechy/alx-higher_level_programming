#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for i in range(my_list):
            new_list[i] = True if my_list[i] % 2 == 0 else False
