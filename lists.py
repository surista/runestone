#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""
import time
from timeit import Timer

def test1():
    start = time.time()
    l = []
    for i in range(1000):
        l = l + [i]
    end = time.time()

    return "%10.9f seconds" % (end-start)


def test2():
    start = time.time()
    l = []
    for i in range(1000):
        l.append(i)
    end = time.time()

    return "%10.9f seconds" % (end-start)

def test3():
    start = time.time()
    l = [i for i in range(1000)]
    end = time.time()

    return "%10.9f seconds" % (end-start)

def test4():
    start = time.time()
    l = list(range(1000))
    end = time.time()

    return "%10.9f seconds" % (end-start)

t1 = Timer("test1()", "from __main__ import test1")
print(f"concatenation: {t1.timeit(number=10000):15.2f} milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print(f"appending: {t2.timeit(number=10000):19.2f} milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print(f"list comprehension: {t3.timeit(number=10000):10.2f} milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print(f"list range: {t4.timeit(number=10000):18.2f} milliseconds")


pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(200000))
print(f"pop(0): {pop_zero.timeit(number=1000):10.5f} milliseconds")

x = list(range(200000))
print(f"pop(): {pop_end.timeit(number=1000):11.5f} milliseconds")

import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")
for i in range(10_000, 1_000_001, 20_000):
    t = timeit.Timer(f"random.randrange({i}) in x",
    "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print(f"{i:<10,}{lst_time:>10.3f}{dict_time:>10.3f}")