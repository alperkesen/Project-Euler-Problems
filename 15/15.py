#!/usr/bin/env python
# coding: utf-8

from math import factorial

def routes(height, width):
    ways = factorial(height + width) \
    / (factorial(width) * factorial(height))
    return ways

answer = routes(20, 20)
print answer

	
