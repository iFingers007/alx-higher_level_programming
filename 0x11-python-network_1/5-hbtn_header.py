#!/usr/bin/python3
"""Python Network 1 Module"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url).headers
    print(resp["X-Request-Id"])
