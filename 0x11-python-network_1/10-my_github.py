#!/usr/bin/python3
"""
Script takes your Github credentials (username and password) and
uses the Github API to display your id.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    tmp_file = requests.get("https://api.github.com/user",
                            auth=(argv[1], argv[2]))
    try:
        print(tmp_file.json().get("id"))
    except ValueError:
        print("None")
