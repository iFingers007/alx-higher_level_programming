#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for elmts in my_list[:x]:
            print("{}".format(elmts), end="")
            printed += 1
    except Exception:
        pass
    print()
    return printed
