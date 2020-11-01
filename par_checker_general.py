#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

def par_checker(par_string):
    s = []
    pares = {'(':')', '{':'}', '[':']'}

    for char in par_string:
        if char in pares:
            s.append(char)
        else:
            if len(s) == 0:
                return False
            else:
                if pares[s.pop()] != char:
                    return False
    return len(s) == 0

print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False
print(par_checker('{({([][])}())}')) # expected True
print(par_checker('[{()]')) #expected false


