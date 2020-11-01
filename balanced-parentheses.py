#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

class Stack:
    "stack implementation as a list"

    def __init__(self):
        "creates a new stack"
        self._items = []

    def is_empty(self):
        'Check if stack is empty'
        return not bool(self._items)

    def push(self, item):
        "adds item to top of stack"
        self._items.append(item)

    def pop(self):
        "removes top item from stack"
        self._items.pop()

    def peek(self):
        "gets - but does not remove - top item"
        return self._items[-1]

    def size(self):
        "returns size of current stack"
        return len(self._items)



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