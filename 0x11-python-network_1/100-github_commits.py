#!/usr/bin/python3
"""Python Network 1 Module"""
import requests
import sys

if __name__ == "__main__":

    repo, owner = sys.argv[1], sys.argv[2]
    url = f" https://api.github.com/{repo}/{owner}/commits"
    params = {'per_page': 10}
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        json_resp = resp.json()

    except requests.RequestException as e:
        print(f"Error: {e}")
