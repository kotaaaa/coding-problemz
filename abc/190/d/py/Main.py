import math
import sys
import collections
from heapq import heappop, heappush


n = int(input())

queue = []
for i in range(1,int(math.sqrt(2*n)+1)):
    if 2*n % i == 0:
        heappush(queue, i)
        if 2*n / i != i:
            heappush(queue, int(2*n / i))
# print(queue)

ans = []
while queue:
    x = heappop(queue)
    a = 0.5*(((2*n)/x) - x+1)
    if float.is_integer(a):
        ans.append(a)

    # print(x, a)

# print(ans)
print(len(ans))



