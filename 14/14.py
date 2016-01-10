#! /usr/bin/env python
# coding: utf-8

def longest_chain(term):
	chain = 0
	while term != 1:
		if term % 2 == 0:
			term /= 2
		elif term % 2 != 0:
			term = term * 3 + 1
		chain += 1
	return chain + 1


answer = 0
number = 0

limit = 1

while limit < 1000000:
	if longest_chain(limit) > answer:
		answer = longest_chain(limit)
		number = limit
	limit += 1

print number