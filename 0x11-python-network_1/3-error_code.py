#!/usr/bin/python3
"""Python Network 1 Module"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as resp:
            data = resp.read().decode('utf-8')
            print(data)
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.status}")
