#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first and second elements from each tuple
    a, b = tuple_a[:2], tuple_b[:2]
    # Pad the tuples with 0 if they have less than 2 elements
    a += (0,) * (2 - len(a))
    b += (0,) * (2 - len(b))
    # Adding the first two results
    result = (a[0] + b[0], a[1] + b[1])
    return result
