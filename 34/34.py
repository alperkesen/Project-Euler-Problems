#! /usr/bin/env python
# coding: utf-8

from math import factorial

answer = 0

for x in xrange(10,100000):
	result = 0
	for y in str(x):
		result += factorial(int(y))
	if result == x:
		answer += x

print answer