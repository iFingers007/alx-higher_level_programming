#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_pop = []
    if value not in a_dictionary.values():
        return a_dictionary
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_pop.append(key)
    print(keys_to_pop)
    for k in keys_to_pop:
        a_dictionary.pop(k)
    return a_dictionary
