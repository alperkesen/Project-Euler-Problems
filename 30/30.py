#!/usr/bin/env python
# coding: utf-8

answer = 0

for x in xrange(2, 1000000):
    digit_sum = 0
    for y in str(x):
        digit_sum += int(y) ** 5
    if digit_sum == int(x):
        answer += int(x)
        print x

print answer
