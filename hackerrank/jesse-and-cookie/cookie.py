#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

## This is TLE, deque insert is O(n), so Overall,O(n^2)

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A


def get_index(val, arr):
    if arr[len(arr) - 1] < val:
        return len(arr)
    if arr[0] > val:
        return 0
    right = len(arr)
    left = 0
    mid = 0
    while left + 1 < right:
        mid = (left + right) // 2
        if val > arr[mid]:
            left = mid
        else:
            right = mid
    return left + 1


def cookies(k, A):
    # Write your code here
    A.sort()
    A = deque(A)
    cnt = 0
    while True:

        min_val = A[0]
        if min_val >= k:
            return cnt

        if len(A) <= 2:
            return -1

        a = A.popleft()
        b = A.popleft()
        idx = get_index(a + b * 2, A)
        A.insert(idx, a + b * 2)

        cnt += 1


if __name__ == "__main__":
    f = open("23.txt", "r")
    d = f.read().split("\n")
    n = int(d[0].split(" ")[0])
    k = int(d[0].split(" ")[1])
    A = [int(i) for i in d[1].split(" ")]

    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    # first_multiple_input = input().rstrip().split()
    # n = int(first_multiple_input[0])
    # k = int(first_multiple_input[1])
    # A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print("result", result)
