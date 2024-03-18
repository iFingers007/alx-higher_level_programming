#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0: #Check for negative index
        return None
    elif idx > len(my_list): #Check for out of range of idx
        return None
    else:
        return idx + 1
