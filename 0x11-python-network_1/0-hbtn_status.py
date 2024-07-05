#!/usr/bin/python3
"""Python Network 1 Module"""

import urllib.request

if __name__ == "__main__":    
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        received = response.read()
    decoded = received.decode("utf-8")
    print(decoded)
