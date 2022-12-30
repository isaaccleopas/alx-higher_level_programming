#!/usr/bin/python3
"""
This module has one function that prints two lines
after any of these characters; '.','?',':'
"""
def text_indentation(text):
    """
    prints two lines after '.', '?' or ':'
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '.' or i == '?' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")

