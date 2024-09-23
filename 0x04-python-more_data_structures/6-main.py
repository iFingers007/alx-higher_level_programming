#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
my_dict = { }
my_dict_0 = { 'languages': "C" }
my_dict_1 = { 'a': "e", 'B': "d" , 'c': "c", 'd': "b", 'E': "a" }
print_sorted_dictionary(my_dict)
print("----")
print_sorted_dictionary(my_dict_0)
print("----")
print_sorted_dictionary(my_dict_1)
print("----")
print_sorted_dictionary(a_dictionary)
