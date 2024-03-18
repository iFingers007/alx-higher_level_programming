#!/usr/bin/python3
def element_at(my_list, idx):
    # Check for negative index and out of range
    if idx < 0 or idx >= len(my_list):
        return None
    # returns the index
    else:
        return my_list[idx]
