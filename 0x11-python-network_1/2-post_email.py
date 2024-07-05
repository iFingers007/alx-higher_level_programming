#!/usr/bin/python3
"""Python Network 1 Module"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    data = urllib.parse.urlencode({"email:" email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(req) as resp:
        data = resp.read()
        decoded = data.decode('utf-8')
        print(decoded)
        