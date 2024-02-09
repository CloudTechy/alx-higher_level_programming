#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for x in range(len(row)):
                if x == len(row) - 1:
                    print("{:d}".format(row[x]))
                    continue
                print("{:d} ".format(row[x]), end="")
    else:
        print("")
