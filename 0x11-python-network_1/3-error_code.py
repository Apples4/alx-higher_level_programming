#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body
"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    data = Request(url)

    try:
        with urlopen(data) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
