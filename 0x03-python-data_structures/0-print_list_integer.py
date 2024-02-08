#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ Prints list of integeres

        args: 
            my_list (list): List of integers
        Returns:
            None: prints the numbers
    """
    for num in my_list:
        print ("{:d}".format(num))

print_list_integer([1,2,3])
