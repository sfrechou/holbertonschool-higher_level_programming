#!/usr/bin/python3
"""
Script that takes 2 arguments in order to solve this challenge
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/" + argv[2] + \
          "/" + argv[1] + "/commits"
    result = requests.get(url)
    if result.status_code == 200:
        try:
            to_json = result.json()
            contador = 0
            for key in to_json:
                if contador < 10:
                    print("{}: {}".format(key['sha'],
                                          key['commit']['author']['name']))
                    contador += 1
        except:
            pass
