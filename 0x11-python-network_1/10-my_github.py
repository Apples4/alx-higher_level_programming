#!/usr/bin/python3
"""
Write a Python script that
takes your GitHub credentials
"""

from sys import argv
import requests

if __name__ == "__main__":

    url = "https://api.github.com/user"
    auth = requests.auth.HTTPBasic(argv[1], argv[2])
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
