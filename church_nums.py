#!/usr/bin/env python3

"""
Church numerals
"""

def zero(f):
    """Return church numeral 0"""
    return lambda x: x

def one(f):
    """Return church numeral 1"""
    return lambda x: f(x)

def successor(n):
    """Return a successor of the given church numeral n"""
    return lambda f: lambda x: f(n(f)(x))

def church_to_int(n):
    """Return the church numeral n as a Python integer"""
    return n(lambda x: x + 1)(0)

def add(m, n):
    """Return the church numeral for m + n, for church numerals m and n."""
    return lambda f: lambda x: m(f)(n(f)(x))

def mul(m, n):
    """Return the church numeral for m * n, for church numerals m and n."""
    return lambda f: lambda x: m(n(f))(x)

def pow(m, n):
    """Return the church numeral for m ** n, for church numerals m and n."""
    return lambda f: lambda x: (n(m))(f)(x)
