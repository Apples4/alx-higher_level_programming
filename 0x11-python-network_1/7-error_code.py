#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the body ofthe response.
"""

from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]

    response = requests.get(url)
    print("Error code: {}".format(response.status_code))
