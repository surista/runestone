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


s = Stack()

print(s.is_empty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
s.pop()
s.pop()
print(s.size())



def rev_string(my_str):
    rev_stack = []
    normal_stack = []
    for x in my_str:
        rev_stack.insert(0, x)
    return ''.join(rev_stack)

print(rev_string('bacon'))