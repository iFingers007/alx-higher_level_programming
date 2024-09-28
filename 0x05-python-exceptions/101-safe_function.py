#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:  # (ValueError, TypeError):
        print(f"Exception: {err}", file=sys.stderr)
        return None
