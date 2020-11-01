#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
"""

import random
class MSDie:
    """
    Multi-side die
    Instance Variables:
        current_value
        num_sides
    """
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_val = self.roll()

    def roll(self):
        self.current_val = random.randrange(1, self.num_sides+1)
        return self.current_val

    def __str__(self):
        return str(self.current_val)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_val)

my_die = MSDie(6)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)