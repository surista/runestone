#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""
import time
import random

def anagram_solution(string1, string2):
    start = time.time()

    if len(string1) != len(string2):
        return False

    for x in string1:
        if x not in string2:
            return False
    end = time.time()
    return True, "%10.9f seconds" % (end-start)


def anagram_solution2(string1, string2):
    start = time.time()

    if len(string1) != len(string2):
        return False

    for x in string1:
        if string1.count(x) != string2.count(x):
            return False
    end = time.time()
    return True, "%10.7f seconds" % (end-start)



print(anagram_solution('pythoabcnabcdefghdddddijkl', 'pythoabcnabcdefghijdddddkl'))# expected: True
print(anagram_solution("aba", "aaa"))  # expected: True
print(anagram_solution("abcd", "dcba"))  # expected: True
print(anagram_solution("abcd", "dcda"))  # expected: False

print(anagram_solution2('pythoabcnabcdefghdddddijkl', 'pythoabcnabcdefghijdddddkl'))# expected: True
print(anagram_solution2("aba", "aaa"))  # expected: True
print(anagram_solution2("abcd", "dcba"))  # expected: True
print(anagram_solution2("abcd", "dcda"))  # expected: False