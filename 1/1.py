#!/usr/bin/env python
# coding: utf-8

answer = 0

for x in xrange(1, 1000):
    if x % 5 == 0 or x % 3 == 0:
        answer += x
        
print answer
