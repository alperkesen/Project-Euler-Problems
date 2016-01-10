#! /usr/bin/env python
# coding: utf-8

first_value = 0
second_value = 0

for x in xrange(1,101):
    first_value += x ** 2
    second_value += x

print second_value ** 2 - first_value