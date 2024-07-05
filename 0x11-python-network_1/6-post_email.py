#!/usr/bin/python3
"""Python Network 1 Module"""

import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    email_data = {'email': email}
    resp = requests.post(url, data=email_data)
    print(resp.text)
