#!/usr/bin/pythoon3
"""
Contains function inherits_from
"""
def inherits_from(obj, a_class):
    """return true if obj is an instance of class that inherited
    directly or indirectly"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
