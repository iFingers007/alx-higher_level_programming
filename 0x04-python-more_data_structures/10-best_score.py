#!/usr/bin/python3
def best_score(a_dictionary):
    def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    dic_vals = list(a_dictionary.keys())
    high_val = dic_vals[0]
    best_key = a_dictionary.get(high_val)
    for k, v in a_dictionary.items():
        if v > high_val:
            high_val = v
            best_key = k
    return best_key
#    best_scr, best_key = -10 ** 9, None
#    if a_dictionary is not None:
#        for key, value in a_dictionary.items():
#            if value > best_scr:
#                best_key = key
#                best_scr = value
#    return best_key
