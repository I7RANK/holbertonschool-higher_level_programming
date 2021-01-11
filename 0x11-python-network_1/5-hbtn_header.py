#!/usr/bin/python3
""" displays the value of the X-Request-Id variable """

import requests
import sys

reply = requests.get(sys.argv[1])
print(reply.headers["X-Request-Id"])
