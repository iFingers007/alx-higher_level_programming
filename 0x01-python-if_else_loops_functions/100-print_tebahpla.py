#!/usr/bin/python3
result = ''
for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2 == 1:
        result += "{:c}".format(char - 32)
        continue
    result += "{:c}".format(char)
print("{}".format(result), end='')
