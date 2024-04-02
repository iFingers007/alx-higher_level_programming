#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for elmts in my_list[:x]:
            print("{}".format(elmts), end="")
        print()
    except:
        print("Unknown Error")
    else:
        return elmts
