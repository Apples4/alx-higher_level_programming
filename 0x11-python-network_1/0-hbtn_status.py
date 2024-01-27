#!/usr/bin/python3
'''
This script fetches https://alx-intranet.hbtn.io/status
'''
from urllib.request import urlopen

if __name__ == "__main__":

    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
    """convert body to str"""
    convert = body.decode("UTF-8")
    print("Body response")
    print("\t- type: {}\n"
          "\t- content: {}\n"
          "\t- utf8 content: {}".
          format(type(body), body, convert))
