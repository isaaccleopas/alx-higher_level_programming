#!/usr/bin/python3
"""
Contains a class BaseGeometry
"""
class BaseGeometry:
    """A class with public attribute"""
    def area(self):
        """Exception when called"""
        raise Exception("area() is not implemented")
