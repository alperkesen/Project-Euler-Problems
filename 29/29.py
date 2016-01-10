#! /usr/bin/env python
# coding: utf-8

all_combinations = []

for x in xrange(2,101):
	for y in xrange(2,101):
		all_combinations.append(x ** y)

print len(set(all_combinations))
