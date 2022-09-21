#!/bin/python3/

import math
import os
import random
import re
import sys


# /
# Complete the 'findMinimumLengthSubarray' function below./
# /
# The function is expected to return an INTEGER./
# The function accepts following parameters:/
#  1. INTEGER_ARRAY arr/
#  2. INTEGER k/
# /
# 尺取法 / しゃくとり法


def findMinimumLengthSubarray(arr, k):
    left = 0
    right = 0
    inf = 10000000
    min_val = inf
    print(arr)
    while right < len(arr):
        if len(set(arr[left : right + 1])) >= k:
            min_val = min(min_val, right + 1 - left)
            left += 1
        else:
            right += 1
    if inf == min_val:
        return -1
    return min_val


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findMinimumLengthSubarray(arr, k)

    fptr.write(str(result) + "\n")

    fptr.close()
