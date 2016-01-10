#! /usr/bin/env python
# coding: utf-8

answer = 0

for x in str(2 ** 1000):
	answer += int(x)

print answer