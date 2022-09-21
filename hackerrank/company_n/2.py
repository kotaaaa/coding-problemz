#!/bin/python3/

import math
import os
import random
import re
import sys


from heapq import heapify, heappush, heappop

# /
# Complete the 'reductionCost' function below./
# /
# The function is expected to return an INTEGER./
# The function accepts INTEGER_ARRAY num as parameter./
# /
# 優先度付きキュー


def reductionCost(num):
    num.sort()
    sum_val = 0
    heapify(num)
    while len(num) > 1:
        a = heappop(num)
        b = heappop(num)
        sum_val += a + b
        heappush(num, a + b)
    return sum_val


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    num_count = int(input().strip())

    num = []

    for _ in range(num_count):
        num_item = int(input().strip())
        num.append(num_item)

    result = reductionCost(num)

    fptr.write(str(result) + "\n")

    fptr.close()
