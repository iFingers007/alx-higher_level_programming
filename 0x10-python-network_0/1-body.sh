#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o temp_body -w "%{http_code}" "$1" | grep -q 200 && cat temp_body; rm temp_body
