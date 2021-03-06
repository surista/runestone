#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""


def par_checker(par_string):
    s = []
    for x in par_string:
        if x == '(':
            s.append(x)
        else:
            if len(s) == 0:
                return False
            else:
                if s.pop() != '(':
                    return False

    return len(s) == 0


print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False