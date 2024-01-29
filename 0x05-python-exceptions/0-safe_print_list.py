#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Parameters:
        my_list (list): The list containing elements to be printed.
                        Empty by default.
        x (int): The number of element to print. Defaults to 0

    Returns:
        int: the number of elements to print
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError as e:
        pass
    except Exception as e:
        pass
    print()
    return count
