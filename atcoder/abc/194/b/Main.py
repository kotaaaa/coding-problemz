import math
import sys
import bisect
import copy 

n= int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

min_a = 1000001
min_a_idx = 1000001
min_b = 1000001
min_b_idx = 1000001
for i in range(n):
    if min_a > a[i]:
        min_a = a[i]
        min_a_idx = i

    if min_b > b[i]:
        min_b = b[i]
        min_b_idx = i

# print(min_a_idx, min_b_idx)
if min_a_idx != min_b_idx:
    print(max(a[min_a_idx], b[min_b_idx]))
else:
    sort_a = copy.copy(a)
    sort_b = copy.copy(b)
    sort_a.sort()
    sort_b.sort()
    # a.sort()
    # b.sort()
    # print("aaa")
    second = min(sort_a[1], sort_b[1])
    if (a[min_a_idx] + b[min_a_idx]) <= second:
        print(a[min_a_idx] + b[min_a_idx])
    else:
        # print(second)
        # print("bbb")
        # if a[min_a_idx] > b[min_b_idx]:
            # print(max(a[min_a_idx],sort_a[1]))
        # if a[min_a_idx] < b[min_b_idx]:            
            # print(max(b[min_b_idx],sort_a[1]))
        
        if a[min_a_idx] == b[min_a_idx]:                        
            # print(sort_a[1],sort_b[1])
            print(min(sort_a[1],sort_b[1]))
        else:
            print(min(max(a[min_a_idx],sort_b[1]), max(b[min_b_idx],sort_a[1])))