#!/usr/bin/python3
"""Python Network 1 Module"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as resp:
        data = resp.read().decode('utf-8')
        print(data)
