#!/usr/bin/python3

""" Module for a function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1
