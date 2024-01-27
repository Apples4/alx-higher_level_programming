#!/usr/bin/python3
from sys import argv
import requests

"""
Write a Python script that takes in a
letter and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    if len(argv[1]) == 0:
        line = " "
    else:
        line = argv[1]
    params = {"q": line}

    response = request.post(url, data=params)
    if response.json() == {}:
        print("No result")
    elif len(response.json()) != 0:
        print("[{}] {}"
              .format(response.json().get("id"),
                      response.json().get("name")))
