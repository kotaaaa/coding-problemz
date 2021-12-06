############
## ダイクストラ, 最短経路， 経路数
############

import collections,sys
from collections import deque
from heapq import heappop, heappush

n,m = map(int,input().split())
mod = 10**9 + 7

if m == 0:
    print(0)
    exit()
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]

g = collections.defaultdict(list)
for frm, to in zip(a, b):
    g[frm].append(to)
    g[to].append(frm)

ans_dict = collections.defaultdict(list)

## ダイクストラ
queue = []
confirmed = [0 for _ in range(n+1)]
cnts = [0 for _ in range(n+1)]
distances = [sys.maxsize for _ in range(n+1)]
queue.append((0,1)) # 距離, 街
distances[1] = 0
cnts[1] = 1
while len(queue) > 0:
    target_cost, target_node = heappop(queue)
    if confirmed[target_node] == 1:
        continue
    confirmed[target_node] = 1
    distances[target_node] = target_cost
    for road in g[target_node]:
        if confirmed[road] == 1: ## and road != n:
            continue
        candidate_distance = 1 + distances[target_node]
    
        if candidate_distance < distances[road]:
            distances[road] = candidate_distance
            cnts[road] = cnts[target_node]
        elif candidate_distance == distances[road]:
            cnts[road] += cnts[target_node]
        heappush(queue, (distances[road], road)) 
# print(distances)
# print(cnts)
print(cnts[n] % mod)