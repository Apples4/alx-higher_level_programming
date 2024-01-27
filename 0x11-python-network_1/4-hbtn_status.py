#!/usr/bin/python3
"""
script that fetches
https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":

    print("Body response:")
    print("\t- type: {}".format(type(requests.get(
          "https://alx-intranet.hbtn.io/status").text)))
    print("\t- content: {}".format(requests.get(
          "https://alx-intranet.hbtn.io/status").text))
