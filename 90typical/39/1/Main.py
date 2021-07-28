############
## ダイクストラ (結局使っていない)
############

import collections, sys
from heapq import heappop, heappush

n = int(input())
mod = 10 ** 9 + 7

ab = [map(int, input().split()) for _ in range(n-1)]
a, b = [list(i) for i in zip(*ab)]

g = collections.defaultdict(list)
for frm, to in zip(a, b):
    g[frm].append(to)
    g[to].append(frm)

ans_dict = collections.defaultdict(list)

## ダイクストラ
queue = []
confirmed = [0 for _ in range(n + 1)]
distances = [sys.maxsize for _ in range(n + 1)]
queue.append((0, 1))  # 距離, 街
distances[1] = 0
while len(queue) > 0:
    target_cost, target_node = heappop(queue)
    if confirmed[target_node] == 1:
        continue
    confirmed[target_node] = 1
    distances[target_node] = target_cost
    for road in g[target_node]:
        if confirmed[road] == 1:
            continue
        candidate_distance = 1 + distances[target_node]
        distances[road] = min(distances[road],candidate_distance)
        heappush(queue, (distances[road], road))
print(distances)