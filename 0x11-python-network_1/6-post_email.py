#!/usr/bin/python3
from sys import argv
import requests

"""
script that takes in a URL,
sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":

    url = argv[1]
    data = {"email": argv[2]}

    response = requests.get(url, params=data)
    print(reponse.text)
