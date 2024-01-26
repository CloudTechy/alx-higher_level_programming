#!/usr/bin/python3

if __name__ == "__main__":

    """ does some math and prints result """

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{:s} + {:s} = {:s}".format(a, b, add(a, b)))
    print("{:s} - {:s} = {:s}".format(a, b, sub(a, b)))
    print("{:s} * {:s} = {:s}".format(a, b, mul(a, b)))
    print("{:s} / {:s} = {:s}".format(a, b, div(a, b)))
