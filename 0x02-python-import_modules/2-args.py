#!/usr/bin/python3

if __name__ == "__main__":
    """prints number and the list of its arguments."""

    import sys

    args = sys.argv
    if len(args) == 1:
        print(".")
    else:
        count = len(args)
        a = "arguments" if count > 2 else "argument"
        print("{} {}:".format(count - 1, a))
        for i in range(1, count):
            print("{}: {}".format(i, args[i]))
