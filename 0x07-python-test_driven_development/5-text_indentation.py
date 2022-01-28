#!/usr/bin/python3
'''Function that prints a text with 2 new lines after each of these characters: ., ? and :'''
def text_indentation(text):
    '''Function that prints a text with 2 new lines after each of these characters: ., ? and :'''
    if (type(text) is not str):
        raise TypeError("text must be a string")
    
    jumps = ['.', '?', ':']
    new_string = ""
    flags = 1

    for s in text:
        if flags == 1:
            if s == ' ':
                continue
            else:
                flags = 0
        if flags == 0:
            if s in jumps:
                new_string += s
                new_string += "\n\n"
                flags = 1
            else:
                new_string += s
    print(new_string, end='')
