#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Fraction class
"""



class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def __add__(self, other):
        new_top = self.num * other.den + other.num*self.den
        new_bottom = self.den * other.den
        a = self.gcd(new_top, new_bottom)
        return Fraction(new_top/a, new_bottom/a)

    def __eq__(self, other):
        return (self.num, self.den) == (other.num, other.den)



my_fraction = Fraction(3,5)

f1 = Fraction(3,4)
f2 = Fraction(3,4)
f1_2 = f1+f2
print(f1_2)
print(f1==f2)
