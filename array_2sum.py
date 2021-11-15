#!/bin/env python
"""
array_2sum.py
This is a simple work interview question answered:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
    Given nums = [2, -11, 15, 7], target = 9,

    Because nums[0] + nums[3] = 2 + 7 = 9,
    return [0, 3].

Answer: using dictionary
The keys are the difference which is target - arr[i]
The value is the index i
So for this example this is how it's going to look:
d = {'7': 0, '20': 1, '-6': 2, '2': 3}

When you get to arr[i], you check if arr[i] was already calculate as difference before,
If it has, then you'll find it as a key, meaning d[arr[i]], so you return both indices :-)

Complexity: o(n) (since you're running on arr only once)
"""


def arr_2sum(arr, num):
    d = {}
    n = len(arr)
    for i in range(0, n):
        difference = num - arr[i]
        d[difference] = i
        if arr[i] in d:
            return [d[arr[i]], i]

    return [-1, -1]


def validate_arr_2sum(arr, num):
    result = arr_2sum(arr, num)
    text = "arr_2sum(" + str(arr) + ", " + str(num) + ") = " + str(result)
    print(text)


def main():
    arr = [2, 7, -11, 15]
    validate_arr_2sum(arr, 9)  # [0, 1]
    arr = [2, -11, 15, 7]
    validate_arr_2sum(arr, 9)  # [0, 3]
    validate_arr_2sum(arr, -4)  # [1, 3]
    validate_arr_2sum(arr, -15)  # [-1, -1]
    arr = [98, 0, -35, 24, 17, -9, 100, 7]
    validate_arr_2sum(arr, 98)  # [0, 1]
    validate_arr_2sum(arr, 99)  # [-1, -1]
    validate_arr_2sum(arr, 91)  # [5, 6]
    validate_arr_2sum(arr, 24)  # only [1, 3], even though you have 17 and 7 later on


if __name__ == '__main__':
    main()
