#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = set()
    tSum = 0
    for elmt in my_list:
        if elmt not in uniques:
            uniques.add(elmt)
            tSum += elmt
    return tSum
