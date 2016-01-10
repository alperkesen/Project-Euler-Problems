#! /usr/bin/env python
# coding: utf-8

from math import sqrt

def divisor_generator(n):
	large_divisors = []
	for i in xrange(1, int(sqrt(n) + 1)):
		if n % i == 0:
			yield i
			if i*i != n and n/i != n:
				large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
		yield divisor

answer = 0
number = 1

while number < 10000:
	divisorsSum = sum(list(divisor_generator(number)))
	real_number = sum(list(divisor_generator(divisorsSum)))
	if real_number == number and number != divisorsSum:
		answer += number
	number += 1


print answer

