#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check for negative index and out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    # returns the index
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
