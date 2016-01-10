#! /usr/bin/env python
# coding: utf-8

answer = 1

for x in xrange(1,21):
    if answer % x != 0:
	    for y in xrange(1,21):
	    	if (answer * y) % x == 0:
	    		answer *= y
	    		break


print answer