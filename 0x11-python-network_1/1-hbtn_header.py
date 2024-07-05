#!/usr/bin/python3
"""Python Network 1 Module"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        pass
    for header, value in resp.headers.items():
        if header == "X-Request-Id":
            print(value)
