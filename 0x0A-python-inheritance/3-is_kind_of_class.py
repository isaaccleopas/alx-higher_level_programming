#!/usr/bin/python3
"""
Contains function is_kind_of_class
"""
def is_kind_of_class(obj, a_class):
    """return true if obj is an instance or inherited from a class, otherwise false"""
    return(isinstance(obj, a_class))

