#!/bin/env python
"""
array_multiplication.py
This is a simple work interview question answered:
assume you have a list (array) of integers,
return a list at the same size, where each element is the multiplication of all other elements.
Example:
    For this array [11, 2, 3, 6, 8] it should return -> [288, 1584, 1056, 528, 396]
    (288 = 2*3*6*8)
    (1584 = 11*3*6*8)
    (and so on...)

The second question is do exactly the same - WITHOUT DIVIDE OPERATOR!!

Both functions complexities should be o(n)
"""


def arr_mul(arr):
    """
    Algorithm (using divide operator):
    First multiply all numbers ("total" variable),
    Then for each element in arr:
        divide the big number (total) with the current element,
        append this number into the result list

    Number of calculations: 2*n
    """
    n = len(arr)
    result = []
    total = 1
    calculations = 0
    for i in arr:
        total *= i
        calculations += 1
    for i in arr:
        result.append(int(total / i))
        calculations += 1

    print("Size of list = " + str(n))
    print("Total calculations = " + str(calculations))
    return result


def arr_mul_no_div(arr):
    """
    Algorithm (without using divide operator):
    Allocate for temp list the number 1 (as first element)
    Then each new element in temp = previous element in temp * arr[i-1].
    (ranges from 1 to n)
    Example:
        arr = [11, 2, 3, 6, 8] -> temp = [1, 11, 22, 66, 396]
        (1 was allocated as first element in temp)
        (11 = 1*11)
        (22 = 11*2)
        (66 = 22*3)
        (396 = 66*6)

    Allocate fore result the number 1 (as last element!!!)
    Then for each new element in result (at location 0!!!) = last added result * arr[i]
    (ranges from n-1 to 0)
    Example:
        arr = [11, 2, 3, 6, 8] -> result = [288, 144, 48, 8, 1]
        (1 was allocated as last element in result
        (8 = 1*8)
        (48 = 8*6)
        (144 = 48*3)
        (288 = 144*2)

    Last loop:
        result[i] = result[i] * temp[i]
        (this way you multiply all elements except for current element :-) )

    Number of calculations: 3*n - 1
    """
    n = len(arr)
    result = [1]
    temp = [1]
    calculations = 0
    for i in range(1, n):
        temp.append(temp[i - 1] * arr[i - 1])
        calculations += 1
    for i in range(n - 1, 0, -1):
        result = [result[0] * arr[i]] + result
        calculations += 1
    for i in range(0, n):
        result[i] = result[i] * temp[i]
        calculations += 1

    print("Size of list = " + str(n))
    print("Total calculations = " + str(calculations))
    return result


def main():
    arr = [11, 2, 3, 6, 8]
    print("arr_mul(" + str(arr) + ")")
    print(arr_mul(arr))

    print("")
    print("arr_mul_no_div(" + str(arr) + ")")
    print(arr_mul_no_div(arr))


if __name__ == '__main__':
    main()
