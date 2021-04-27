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

def triMulti(mylist):
    mylist.sort()
    l = len(mylist)
    m1 = mylist[l-1] * mylist[l-2] * mylist[l-3] # [-5, -4, 0, 10, 20, 30, 40] or [-10, -7, -5, -1]
    m2 = mylist[0]   * mylist[1]   * mylist[l-1] # [-10,-5, 0, 1, 2, 3]
    return max(m1,m2)
    

def main():
    print(triMulti([4,5,1])) #20
    print(triMulti([30, -4, 10, 40, 20, -5, 0])) #24000
    print(triMulti([1, 0,-5 ,2 ,3, -10])) #150
    print(triMulti([-1, 0, 1, 2])) #0
    print(triMulti([-10, -7, -5, -1])) #-35
    

if __name__ == '__main__':
    main()
