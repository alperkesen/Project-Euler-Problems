#! /usr/bin/env python
# coding: utf-8

from math import factorial

answer = 0

for x in str(factorial(100)):
	answer += int(x)

print answer