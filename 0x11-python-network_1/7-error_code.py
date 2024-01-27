#!/usr/bin/python3
from sys import argv
import requests

"""
script that takes in a URL,
sends a request to the URL
and displays the body ofthe response.
"""

if __name__ == "__main__":

    url = argv[1]

    response = requests.get(url)
    print("Error code: {}".format(response.status_code))
