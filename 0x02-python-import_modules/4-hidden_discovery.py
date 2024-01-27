#!/usr/bin/python3

if __name__ == "__main__":

    """ Prints the definitions in a module """

    import hidden_4

    hidden_names = dir(hidden_4)

    sorted_names = sorted(hidden_names)

    for name in sorted_names:
        if name[0] != "_":
            print(name)
