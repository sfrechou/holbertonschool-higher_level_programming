#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""
import requests


request = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\t- content: {}"
      .format(type(request.text), request.text))
