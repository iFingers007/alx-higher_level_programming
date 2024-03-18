#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        result = 0
    else:
        result = sum(int(arg) for arg in argv[1:])

    print("{:d}".format(result))
