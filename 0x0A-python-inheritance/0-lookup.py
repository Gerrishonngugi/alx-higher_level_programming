#!/usr/bin/python3
"""
The lookup module
"""


def lookup(obj):
    """
    Returns the list of available methods and attributes of an object.
    """
    return dir(obj)
