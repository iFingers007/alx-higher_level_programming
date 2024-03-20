#!/usr/bin/python3
def best_score(a_dictionary):
    best_scr, best_key = -10 ** 9, None
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if value > best_scr:
                best_key = key
                best_scr = value
    return best_key
