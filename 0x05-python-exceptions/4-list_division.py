#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 list.

    Args:
        my_list_1 (list): The no 1  list.
        my_list_2 (list): The no 2 list.
        list_length (int): The number of elements to resultide.

    Returns:
        A new list of length list_length containing all the division.
    """
    result_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return (result_list)
