#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    """ imports the add module """

    a = 1
    b = 2
    sum = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))
