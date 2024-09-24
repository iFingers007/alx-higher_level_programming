#!/usr/bin/python3
def roman_to_int(roman_string):
    summed = []
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev_value = 0
    total = 0
    for char in roman_string:
        if char in roman_dict:
            summed.append(int(roman_dict[char]))
    for num in reversed(summed):
        if num < prev_value:
            total -= num
        else:
            total += num
        prev_value = num
    return total
