#!/bin/env python
"""
tri_multi.py
Purpose: function gets a list of integers (at least 3 numbers), 
         and returns the largest 3 numbers multiplication
Usage:
    python tri_multi.py
Author: Dovi Klausner
Date: 04/2021
"""
import sys


def triMulti(mylist):
    """
    Disadvantage: complexity is o(log n) because of sort()
    Advantage: verrrry short to code
    """
    mylist.sort()
    l = len(mylist)
    m1 = mylist[l - 1] * mylist[l - 2] * mylist[l - 3]  # [-5, -4, 0, 10, 20, 30, 40] or [-10, -7, -5, -1]
    m2 = mylist[0] * mylist[1] * mylist[l - 1]  # [-10,-5, 0, 1, 2, 3]
    return max(m1, m2)

def tryMultiBetter(arr):
    """
    Disadvantage: a bit longer to code
    Advantage: complexity is o(n)
    """
    # max1 > max2 > max3
    # min2 > min1
    max1 = max2 = max3 = -sys.maxsize
    min1 = min2 = sys.maxsize
    for i in arr:
        if i > max3:
            max3 = i
            if i > max2:
                max3 = max2
                max2 = i
                if i > max1:
                    max2 = max1
                    max1 = i

        if i < min2:
            min2 = i
            if i < min1:
                min2 = min1
                min1 = i

    m1 = max1 * max2 * max3
    m2 = min1 * min2 * max1
    return max(m1, m2)

def main():
    print(triMulti([4, 5, 1]))  # 20
    print(tryMultiBetter([4, 5, 1]))  # 20
    print(triMulti([30, -4, 10, 40, 20, -5, 0]))  # 24000
    print(tryMultiBetter([30, -4, 10, 40, 20, -5, 0]))  # 24000
    print(triMulti([1, 0, -5, 2, 3, -10]))  # 150
    print(tryMultiBetter([1, 0, -5, 2, 3, -10]))  # 150
    print(triMulti([-1, 0, 1, 2]))  # 0
    print(tryMultiBetter([-1, 0, 1, 2]))  # 0
    print(triMulti([-10, -7, -5, -1]))  # -35
    print(tryMultiBetter([-10, -7, -5, -1]))  # -35


if __name__ == '__main__':
    main()
