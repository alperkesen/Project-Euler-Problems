#!/usr/bin/env python
# coding: utf-8

from math import factorial

permutation = ""
numbers=[x for x in "0123456789"]
start = 9
nth_permutation = 0
limit = 1000000

while nth_permutation != limit and start >= 0:
    for x in xrange(0,10):
        try_permutation = x * factorial(start)
        other_permutation = (x-1) * factorial(start) 
        if try_permutation >= limit - nth_permutation:
            if start != 0 and other_permutation + nth_permutation == limit:
                nth_permutation += (x-2) * factorial(start)
                permutation += str(numbers[x-2])
                print str(numbers[x-2])
                numbers.remove(numbers[x-2])
                break
            else:
                nth_permutation += (x-1) * factorial(start)
                permutation += str(numbers[x-1])
                print str(numbers[x-1])
                numbers.remove(numbers[x-1])
                break
    start -= 1

print permutation

"""0123 0132 0213 0231 0312 0321 1023 1032 1203 1230 1302 1320
2013 2031 2103 2130 2301 2310 3012 3021 3102 3120 3201 3210 

012 021 102 120 201 210"""

