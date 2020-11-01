#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Fraction class
"""


class Fraction:
    def __init__(self, num, den):
        a = self.gcd(num, den)
        self.num = num/a
        self.den = den/a

    def __str__(self):
        return f"{self.num}/{self.den}"

    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def __add__(self, other):
        new_top = self.num * other.den + other.num*self.den
        new_bottom = self.den * other.den
        return Fraction(new_top, new_bottom)

    def __eq__(self, other):
        return (self.num, self.den) == (other.num, other.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den
