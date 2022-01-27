#!/usr/bin/python3
'''Function that prints a text with 2 new lines after each of these characters: ., ? and :'''
def text_indentation(text):
    '''Function that prints a text with 2 new lines after each of these characters: ., ? and :'''
    if (type(text) is not str):
        raise TypeError("text must be a string")
    
    jumps = ['.', '?', ':']
    new_string = ""
    flags = 0
    for s in text:
        new_string += s
        if s in jumps:
            new_string += "\n\n"
            flags = 1
        else:
            flags = 0
    print(new_string, end="")
