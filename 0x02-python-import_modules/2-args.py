#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1  # Subtract 1 to exclude the script name

    if argc == 0:
        print("0 arguments.")
    else:
        print("{:d} {}:".format(
            argc,
            'argument' if argc == 1 else 'arguments'))
        for i in range(1, argc + 1):
            print(f"{i}: {argv[i]}")
