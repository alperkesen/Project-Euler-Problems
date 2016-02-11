#! /usr/bin/env python
# coding: utf-8

from math import sqrt, ceil

answer = 0
triangle = 1
raise_amount = 1

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

while True:
    if len(list(divisorGenerator(triangle))) > 500:
        answer = triangle
        break
    else:
        raise_amount += 1
        triangle += raise_amount

print answer

