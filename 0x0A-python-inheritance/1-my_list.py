#!/usr/bin/python3

""" Module for my_list class



"""


class MyList(list):
    """ List subclass that inherits list attributes
    """
    def print_sorted(self):
        """ Prints the list, but sorted
        """
        sorted_list = sorted(self)
        print(sorted_list)
