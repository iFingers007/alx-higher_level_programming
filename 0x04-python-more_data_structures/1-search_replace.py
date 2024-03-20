#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for word in my_list:
        if word == search:
            new_list.append(replace)
        else:
            new_list.append(word)
    return new_list
