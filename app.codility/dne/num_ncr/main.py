# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from operator import mul
from functools import reduce


def ncr(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def solution(A):
    # write your code in Python 3.8.10
    num_dict = {}
    for i in A:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    sum_val = 0
    for i in num_dict.keys():
        if num_dict[i] < 2:
            continue
        sum_val += ncr(num_dict[i], 2)
    return sum_val
