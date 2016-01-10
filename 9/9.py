#! /usr/bin/env python
# coding: utf-8

first_value = 1
answer = 0

while first_value < 1000:
	for x in xrange(first_value, 1000 - first_value + 1):
		if first_value ** 2 + x ** 2 == (1000 - first_value - x) ** 2:
			answer = first_value * x * (1000 - first_value - x)
	first_value +=1

print answer
