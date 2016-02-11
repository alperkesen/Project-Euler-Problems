#! /usr/bin/env python
# coding: utf-8

nth_prime_number = 1
prime_number = 2
prime_number_list = [2]

while nth_prime_number < 10001:
    for prime in prime_number_list:
        if prime_number % prime == 0:
            break
        else:
            if prime == prime_number_list[-1]:
                prime_number_list.append(prime_number);
                nth_prime_number += 1

    prime_number += 1

answer = prime_number - 1
print answer

