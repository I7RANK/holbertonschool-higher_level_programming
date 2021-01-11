#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL """
import requests
import sys


data = {"email": sys.argv[2]}

req = requests.post(sys.argv[1], data=data)

print(req.text)
