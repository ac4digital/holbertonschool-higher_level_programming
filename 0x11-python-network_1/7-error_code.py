#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL & displays
the body of the response.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    tmp_file = requests.get(argv[1])
    if tmp_file.status_code >= 400:
        print("Error code: {}".format(tmp_file.status_code))
    else:
        print(tmp_file.text)
