#!/usr/bin/python3
"""Get https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
    if "ok" in r.text.lower():  # Check if "ok" is present anywhere in the response      
        print("\t- Content:", r.text[:50])  # Print the first 50 characters of the response

