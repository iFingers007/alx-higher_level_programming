#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if character is a lower case
        if 'a' <= char <= 'z':
            # Convert from lower case to upper
            upper = chr(ord(char) - ord('a') + ord('A'))
            result += upper
        else:
            result += char
    print("{}".format(result))
