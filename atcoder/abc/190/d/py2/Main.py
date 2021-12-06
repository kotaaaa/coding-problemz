import math
import sys
from heapq import heappop, heappush


n = int(input())
# print(n)
res=set()
queue = []
# for i in range(1,math.ceil((math.sqrt(n)))):
i = 1
while (i*i<=2*n):
    if 2*n % i == 0:
        heappush(queue, i)
        res.add(i)
        # if n / i != i:
        # heappush(queue, int(n / i))
        res.add(2*n // i)
    i+=1
# print(queue)

ans = []
ans_num = 0
# while queue:
for x in res:
    # x = heappop(queue)
    # a = 0.5*(((2*n)/x) - x+1)
    # if float.is_integer(a):
        # ans.append(a)
    m = 2*n // x
    # if x % 2 == 1: # odd num
    #     if m % 2 == 0:
    #         ans_num += 1
    # else: # even num 
    #     if m % 2 == 1:
    #         ans_num += 1
    if (x-m)%2 == 1:
        ans_num+=1
    # print(x, a)

# print(ans)
# print(len(ans)+1)
print(ans_num)



