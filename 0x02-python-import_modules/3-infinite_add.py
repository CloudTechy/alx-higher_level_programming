#!/usr/bin/python3

if __name__ == "__main__":
    """prints the total of all arguments."""

    import sys

    args = sys.argv
    result = 0
    count = len(args)
    if count > 1:
        result = sum(int(args[i]) for i in range(1, count))
    print(result)
