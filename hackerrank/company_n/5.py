#!/bin/python3/

import math
import os
import random
import re
import sys


# /
# Complete the 'runningMedian' function below./
# /
# The function is expected to return an INTEGER_ARRAY./
# The function accepts INTEGER_ARRAY arr as parameter./
# Getting max value from Priority Queue.

# 空の初期配列に要素を追加していった際、それぞれの数列の中央値を求める。
# 優先度付きキュー

from heapq import heapify, heappop, heappush


def runningMedian(arr):
    h1 = [float("inf")]
    h2 = [float("inf")]
    res = [0 for _ in range(len(arr))]
    med = arr[0]
    for i in range(len(arr)):

        h1_max = -h1[0]
        h2_min = h2[0]
        if len(h1) == len(h2):
            if arr[i] > h2_min:
                heappush(h1, -heappop(h2))
                heappush(h2, arr[i])
            else:
                heappush(h1, -arr[i])
        else:
            if arr[i] < h1_max:
                heappush(h2, -heappop(h1))
                heappush(h1, -arr[i])
            else:
                heappush(h2, arr[i])
        if len(h1) >= len(h2):
            res[i] = -h1[0]
        else:
            res[i] = h2[0]

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = runningMedian(arr)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
