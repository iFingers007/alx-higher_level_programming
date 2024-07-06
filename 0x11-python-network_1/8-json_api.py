#!/usr/bin/python3
"""Python Network 1 Module"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': q}

    try:
        resp = requests.post(url, data=payload)
        resp.raise_for_status()
        try:
            json_resp = resp.json()
            if json_resp:
                print(f"[{json_resp.get('id')}] {json_resp.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.RequestException as e:
        print(f"Error: {e}")
