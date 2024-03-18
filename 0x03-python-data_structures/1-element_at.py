#!/usr/bin/python3
def element_at(my_list, idx):
    # Check for negative index
    if idx < 0:
        return None
    # Check for out of range of idx
    elif idx > len(my_list):
        return None
    else:
        return idx + 1
