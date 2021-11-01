############
## SCC 強連結成分分解
############
from collections import defaultdict
n, m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]

import sys
sys.setrecursionlimit(10**9)

g = defaultdict(set)
g2 =defaultdict(set)
for frm, to in zip(a, b):
    g[frm].add(to)
    g2[to].add(frm)

## 1回目のDFS
visited = [0 for _ in range(n+1)]
orders = []
def dfs(node):
    visited[node] = 1
    for i in g[node]:
        if visited[i] > 0:
            continue
        dfs(i)
    orders.append(node)
    return 

for i in range(n):
    if visited[i] > 0:
        continue
    dfs(i)
# print("orders",orders)
visited = [0 for _ in range(n+1)]
groups = defaultdict(set)
def dfs2 (node, label):
    visited[node] = 1
    groups[label].add(node)
    for i in g2[node]:
        if visited[i] > 0:
            continue
        dfs2(i, label)
    return

## 2回目のDFS 
label = 0
for target in reversed(orders):
    if visited[target] > 0:
        continue
    ret = dfs2(target, label)
    label += 1
ans = 0
# print(groups)
for k,v in groups.items():
    g_size = len(v)
    # if g_size <= 1:
        # continue
    ans += g_size*(g_size - 1) // 2
print(ans)