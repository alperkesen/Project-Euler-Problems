#!/usr/bin/env python
# coding: utf-8

answer = 0

for x in xrange(100,1000):
    for y in xrange(100, 1000):
        if (x * y > answer and str(x*y) == str(x*y)[::-1]):
        answer = x*y

print answer 