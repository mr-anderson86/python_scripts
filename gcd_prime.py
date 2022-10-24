#!/bin/env python
"""
gcd_prime.py
Purpose: function gets 2 integers, 
         and returns the greatest common divisor (gcd) which is also a prime number (or 1, if no gcd).
         Code complexity: o(sqrt(min(a,b)))

         Examples:
            gcdPrime(11, 99) = 11
            gcdPrime(14, 49) = 7
            gcdPrime(3, 7) = 1
            gcdPrime(4, 6) = 2

Usage:
    python gcd_prime.py

Author: Dovi Klausner
Date: 10/2022
"""

import math

def runDivide(x,y):
    while x % y == 0:
        x = x / y
    return x

def gcdPrime(a,b):
    x = a
    y = b
    gcd = 1

    if x % 2 == 0 and y % 2 == 0:
        gcd = 2
    x = runDivide(x,2)
    y = runDivide(y,2)

    # a and b must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    i = 3
    while i < math.sqrt(a)+1 and i < math.sqrt(b)+1 and x > 1 and y > 1:
        if x % i == 0 and y % i == 0:
            gcd = i
        x = runDivide(x,i)
        y = runDivide(y,i)
        i += 2

    # if x and y are bigger than 2, and dividing each other,
    # it means the minimum of them is the gratest common prime divisor
    if x > 2 and y > 2 and max(x,y) % min (x,y) == 0:
        gcd = int(min(x,y))

    return gcd

def test(a, b, expected):
    gcd = gcdPrime(a, b)
    print("gcdPrime({}, {}) = {}".format(a, b, gcd))
    assert gcd == expected

def main():
    test(11, 99, 11)
    test(14, 49, 7)
    test(3, 7, 1)
    test(4, 6, 2)
    test(100, 60, 5)
    test(60, 100, 5)
    test(6, 35, 1)
    test(21, 350, 7)
    test(1010, 505, 101)
    test(1000000000, 1000000000, 5)
    test(999999937, 999999937, 999999937) # largest prime number before 10 billion...
    test(999999937, 999999938, 1)
    test(2 ,2 ,2)
    test(1, 1, 1)


if __name__ == '__main__':
    main()
