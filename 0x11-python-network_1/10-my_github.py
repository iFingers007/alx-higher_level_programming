#!/usr/bin/python3
"""Python Network 1 Module"""
import requests
import sys

if __name__ == "__main__":

    username, password = sys.argv[1], sys.argv[2]
    url = 'https://api.github.com/user'
    try:
        resp = requests.get(url, auth=(username, password))
        resp.raise_for_status()
        json_resp = resp.json()
        print(json_resp.get('id'))
    except requests.RequestException:
        print(f"None")
