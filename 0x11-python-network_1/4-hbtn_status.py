#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    tmp_file = requests.get('https://intranet.hbtn.io/status')
    text = tmp_file.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
