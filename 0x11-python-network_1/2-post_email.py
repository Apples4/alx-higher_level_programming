#!/usr/bin/python3
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

"""
Write a Python script that takes in a URL,
sends a request to the URL
and displays the value
"""
if __name__ == "__main__":

    url = argv[1]
    value = {'email': argv[2]}

    data = urlencode(value)
    data = data.encode('ascii')
    post = Request(url, data)
    with urlopen(post) as response:
        print(response.read().decode('utf-8'))
