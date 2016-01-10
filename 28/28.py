#! /usr/bin/env python
# coding: utf-8

answer = 0
number = 1
raise_amount = 2
circle = 0

while number <= 1002001:
	answer += number
	if circle == 4 :
		circle = 1
		raise_amount += 2
	else:
		circle += 1
	number += raise_amount

print answer
