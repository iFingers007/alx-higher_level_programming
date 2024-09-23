#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ''' Using List comprehension '''
    return [replace if elm == search else elm for elm in my_list]
#    new_list = []
#    for word in my_list:
#        if word == search:
#            new_list.append(replace)
#        else:
#            new_list.append(word)
#    return new_list
