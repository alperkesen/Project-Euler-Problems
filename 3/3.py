#! /usr/bin/env python
# coding: utf-8

given_number = 600851475143
answer = 0

while given_number > 1:
    for x in xrange(2, given_number + 1):
    	if given_number % x == 0:
    	    given_number = given_number / x
    	    answer = x
            break

print answer 
