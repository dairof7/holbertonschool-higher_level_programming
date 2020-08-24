#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import requests

if __name__ == '__main__':
    URL = 'https://intranet.hbtn.io/status'
    req = requests.get(URL)
    error_code = req.status_code
    if error_code >= 400:
        print('Error code: {}'.format(error_code))
    else:
        print(req.text)
