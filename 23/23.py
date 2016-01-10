#! /usr/bin/env python
# coding: utf-8

from math import sqrt

def is_abundant(n):
	divisorSum = 0
	for i in xrange(1, int(sqrt(n) + 1)):
		if n % i == 0:
			divisorSum += i
			if i*i != n and n/i != n:
				divisorSum += n/i
	return divisorSum > n

limit = 28123

number = 1

abundant_list = [x for x in range(1, 28123 + 1) if is_abundant(x)]
abundants = set(abundant_list)

def is_abundant_sum(n):

	for x in abundants:
		if x > n:
			return False
		if n-x in abundants:
			return True			
	return False

sum_of_non_abundant = sum(x for x in xrange(1, limit + 1)
	if not is_abundant_sum(x))

print sum_of_non_abundant
