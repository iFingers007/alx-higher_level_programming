#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:  # (ValueError, TypeError):
        print(f"Exception: {err}", file=sys.stderr)
        return False
