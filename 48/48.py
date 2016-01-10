#! /usr/bin/env python
# coding: utf-8

answer = 0

for x in xrange(1, 1001):
	answer = int(str(answer)[-10:]) +  int(str(x**x)[-10:])

print answer