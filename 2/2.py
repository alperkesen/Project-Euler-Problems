#! /usr/bin/env python
# coding: utf-8

first_value = 1
second_value = 1
even_value = 0

while (first_value < 4000000 and second_value < 4000000):
    if first_value % 2 == 0:
        even_value += first_value
    first_value, second_value = first_value + second_value, first_value 

print even_value
