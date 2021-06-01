import math
import sys 
import collections
from heapq import heappop, heappush

h,w = map(int,input().split())
mass = [list(map(str, input().split())) for _ in range(h)]
# print(mass)

ans = 0
for i in range(0,h-1):
    # print("i",i)
    for j in range(0,w-1):
        num = 0
        # print(mass[i][0][j])
        if mass[i][0][j] == '#':
            num += 1
        if mass[i+1][0][j] == '#':
            num += 1
        if mass[i][0][j+1] == '#':
            num += 1
        if mass[i+1][0][j+1] == '#':
            num += 1

        # print(num)
        if num == 1 or num == 3:
            ans += 1
print(ans)

