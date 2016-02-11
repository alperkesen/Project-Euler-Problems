#!/usr/bin/env python
# coding: utf-8

digit_limit = 1000
first_value = 1
second_value = 1
nth_value = 2

while len(str(first_value)) != 1000:
    first_value, second_value = first_value + second_value, first_value
    nth_value += 1

print nth_value