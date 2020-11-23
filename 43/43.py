#!/usr/bin/env python
# -*- coding: utf-8 -*-


import itertools


def check_divisibility(number):
    if not int(number[1:4]) % 2 == 0:
        return False

    if not int(number[2:5]) % 3 == 0:
        return False

    if not int(number[3:6]) % 5 == 0:
        return False

    if not int(number[4:7]) % 7 == 0:
        return False

    if not int(number[5:8]) % 11 == 0:
        return False

    if not int(number[6:9]) % 13 == 0:
        return False

    if not int(number[7:10]) % 17 == 0:
        return False

    return True


def main():
    pandigital_iterator = iter(itertools.permutations(range(10)))
    total_sum = 0

    for pandigital in pandigital_iterator:
        pandigital = "".join([str(x) for x in pandigital])
        if pandigital[0] != '0' and check_divisibility(pandigital):
            total_sum += int(pandigital)

    print("Total sum:", total_sum)


if __name__ == "__main__":
    print(check_divisibility("1406357289"))
    main()
