#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv

"""
Write a Python script that takes in a URL,
sends a request to the URL
and displays the value
"""
if __name__ == "__main__":

    with urlopen(argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))
