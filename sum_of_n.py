#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""
import time
import random


def sum_of_n_2(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()
    return end-start

x = 0
for i in range(5):
    y = sum_of_n_2(1000)
    x += y

def sum_of_n_3(n):
    return (n * (n + 1)) / 2
#
# print(sum_of_n_3(10))
# print("Average time required is %10.9f seconds" % (x/10))


def find_min(x):
    start = time.time()
    x = [random.randrange(100) for i in range(x)]
    min = 9999999
    for item in range(len(x)):
        if x[item] < min:
            min = x[item]

    end = time.time()
    return min, "%10.9f seconds" % ((end-start)/10)

# print(find_min(100))

def find_min2(x):
    start = time.time()
    x = [random.randrange(100) for i in range(x)]
    min = 9999999
    for a in x:
        for b in x:
            if a < b:
                min = a
    end = time.time()
    return min, "%10.9f seconds" % ((end-start)/10)

print(find_min(10000))
print(find_min2(10000))
