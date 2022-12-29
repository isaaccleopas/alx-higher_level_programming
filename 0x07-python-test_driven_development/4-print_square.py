#!/usr/bin/python3
"""
This is for 4-print_square module and it has one
function print_square()
"""
def print_square(size):
    """
    prints a square with "#" that has the length of size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")

