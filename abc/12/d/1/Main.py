import math
import sys 
from heapq import heappop, heappush

n,m = map(int,input().split())

A = [0] * m
B = [0] * m
T = [0] * m

cost = [[0 for i in range(n+1)] for j in range(n+1)]
path = [[] for i in range(n+1)]

for i in range(m):
    #上から順番に代入していく
    A[i], B[i], T[i] = map(int, input().split())
    path[A[i]].append(B[i])
    path[B[i]].append(A[i])
    cost[A[i]][B[i]] = T[i]
    cost[B[i]][A[i]] = T[i]

ans_dict = [0 for i in range(n+1)]
for i in range(1,n+1):

    queue = []
    confirmed = [0 for i in range(n+1)]
    distances = [10000 for i in range(n+1)]

    queue.append((0,i))
    distances[i] = 0
    while len(queue) > 0:
        target_cost, target_node = heappop(queue)
        confirmed[target_node] = 1
        for road in path[target_node]:
            if confirmed[road] == 1:
                continue
            if (cost[target_node][road] + distances[target_node] < distances[road]):
                distances[road] = min(cost[target_node][road] + distances[target_node], distances[road])
                heappush(queue, (distances[road], road))
        ans_dict[i] = max (distances[target_node], ans_dict[i])
    
print(min(ans_dict[1:]))