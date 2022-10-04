#!/bin/python3

import math
import os
import random
import re
import sys

# https://leetcode.com/discuss/interview-question/1759431/amazon-oa-sum-of-server-powers

#
# Complete the 'findTotalPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY power as parameter.
#
import itertools


def findTotalPower(power):
    res, S, A = 0, [0], [0] + power + [0]
    P = list(itertools.accumulate(itertools.accumulate(A), initial=0))  # O(N)
    for r in range(len(A)):  # O(N)
        while A[S[-1]] > A[r]:  # O(1) amortized
            l, i = S[-2], S.pop()
            res += A[i] * ((i - l) * (P[r] - P[i]) - (r - i) * (P[i] - P[l]))
        S.append(r)
    return res % (10 ** 9 + 7)
    # Write your code here


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    power_count = int(input().strip())

    power = []

    for _ in range(power_count):
        power_item = int(input().strip())
        power.append(power_item)

    result = findTotalPower(power)

    fptr.write(str(result) + "\n")

    fptr.close()
