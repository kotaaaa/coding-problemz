############
## 幅優先探索, 最短経路
############

import collections
from collections import deque

n = int(input())
ab = [map(int, input().split()) for _ in range(n-1)]
a, b = [list(i) for i in zip(*ab)]

g = collections.defaultdict(list)
for frm, to in zip(a, b):
    g[frm].append(to)
    g[to].append(frm)

q = deque()
visited = [0 for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
q.append(1)
ansz = [1]
ansz2 = []
before = 0
while len(q) > 0:
    target = q.popleft()
    if visited[target] == 1:
        continue
    visited[target] = 1
    for node in g[target]:
        if visited[node] == 1:
            continue
        distance[node] = distance[target] + 1
        if distance[node] % 2 == 0:
            ansz.append(node)
        else:
            ansz2.append(node)
        q.append(node)

# print(distance)
if len(ansz) >= n//2:
    for i in range(n//2):
        print(ansz[i],end=" ")
else:
    for i in range(n//2):
        print(ansz2[i],end=" ")

