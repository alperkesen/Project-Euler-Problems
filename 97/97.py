#!/usr/bin/env python
# coding: utf-8

answer = 0
digit = 0
number = 1

while digit < 7830457:
    number = int(str(number)[-11:]) * 2
    digit += 1

print int(str(number * 28433 + 1)[-10:])