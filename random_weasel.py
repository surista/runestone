#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Write a function that generates a random 28 character string
and sees how close it is to a sentence of Shakespeare
"""

import random
import string

def random_weasel(n):
        a = string.ascii_lowercase+' '
        return ''.join(random.choices(a, k=n))

def edit_distance(source, target):
    """
    target: string from random_weasel
    source: "methinks it is like a weasel"
    returns: the minimum edit distance between two strings
    """
    # build matrix of correct size with all values set to 0
    # we add one to length for the '#' placeholder at the start of each string
    sol = [[0 for x in range(len(target)+1)] for y in range(len(source)+1)]

    # initialize first row
    for row in range(len(target)+1):
        for col in range(1):
            sol[0][row] = row

    # initialize first column
    for row in range(len(source)+1):
        for col in range(1):
            sol[row][0] = row

    # compare each letter in target to each letter in source
    # if letters are the same, carry over x-1,y-1 value
    # if letters are different, take minimum of one up and one left and add 1
    for row in range(len(source)):
        for col in range(len(target)):
            if source[row] == target[col]:  # if same, carry over x-1,y-1 value
                sol[row+1][col+1] = sol[row][col]
            else:
                sol[row+1][col+1] = (min(sol[row+1][col], sol[row][col+1]))+1
    return ((sol[len(source)][len(target)]), source)


def generate_scores(n, k):
    """
    repeatedly generate and call random weasel
    Keep best score
    """
    best_score = 9999
    best_string = ""
    count = 0
    for x in range(n):
        if count % 100000 == 0:
            print(best_score, best_string, count)
        test_result = edit_distance(random_weasel(len(k)), k)
        test_score, test_string = test_result[0], test_result[1]
        if test_score < best_score:
            best_score = test_score
            best_string = test_string
        if best_score == 0:
            return best_score, best_string, count
        count += 1
    return best_score, best_string

sol = generate_scores(1000, 'dogs')
print(sol)

