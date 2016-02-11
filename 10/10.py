#!/usr/bin/env python
# coding: utf-8

answer = 0

def prime_numbers(limit):
    prime_list = [True] * 2000000
    prime_list[0] = prime_list[1] = False
    for (x, y) in enumerate(prime_list):
        if y:
            yield x
            for z in xrange(x * x, limit, x):
                prime_list[z] = False

for x in prime_numbers(2000000):
    answer += x

print answer