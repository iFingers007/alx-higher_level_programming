#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        print(f"{k}:{a_dictionary[k]}")
    # Step 1: Extract Keys
#    keys = list(a_dictionary.keys())
    # 2: Sort Keys
#    keys.sort()
    # 3: Iterate over loop and print key, value pair
#    for key in keys:
#        print(key + ": " + str(a_dictionary[key]))
