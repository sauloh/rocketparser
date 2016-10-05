#!/usr/bin/python3

# Simple parser to enumerate names using the RocketReach API
# Usage: ./rocketparser <company-name>

import requests
import json
import sys

API_KEY = "3E7k0123456789abcdef0123456789abcdef" # Sample API from the site - You should use your own
URL = "https://api.rocketreach.co/v1/api/search"

company_name = sys.argv[1]

r = requests.get("{0}/?api_key={1}&company={2}".format(URL, API_KEY, company_name)).text

profiles = json.loads(r)['profiles']

for p in profiles:
	print(p['name'])

