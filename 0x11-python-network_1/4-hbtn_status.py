#!/usr/bin/python3
import requests

"""
script that fetches
https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":

    print("Body response:")
    print("\t- type: {}".format(type(requests.get(
          "https://alx-intranet.hbtn.io/status").text)))
    print("\t- content: {}".format(requests.get(
          "https://alx-intranet.hbtn.io/status").text))
