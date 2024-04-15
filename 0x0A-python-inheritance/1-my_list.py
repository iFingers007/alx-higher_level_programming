#!/usr/bin/python3

""" Module for my_list class



"""


class MyList(list):
    """ List subclass that inherits list attributes

    Args:
    list: Super class

    """
    def print_sorted(self):
        """ Prints the list, but sorted
        """
        print(sorted(self))
