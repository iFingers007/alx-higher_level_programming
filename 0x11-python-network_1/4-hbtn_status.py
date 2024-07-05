#!/usr/bin/python3
"""Python Network 1 Module"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url).text
#    decoded = resp.text
    print("Body response:")
    print(f"\t- type: {type(resp)}")
    print(f"\t- content: {resp}")

