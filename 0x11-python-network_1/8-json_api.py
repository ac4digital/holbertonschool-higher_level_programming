#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    tmp_file = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        tmp_dict = tmp_file.json()
        id = tmp_dict.get('id')
        name = tmp_dict.get('name')
        if len(tmp_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(tmp_dict.get('id'), tmp_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
