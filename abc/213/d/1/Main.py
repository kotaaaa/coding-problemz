from collections import deque
import collections
from heapq import heappop, heappush

import sys
sys.setrecursionlimit(10**9)

# import heapq
n = int(input())
ab = [map(int, input().split()) for _ in range(n-1)]
a, b = [list(i) for i in zip(*ab)]

# ab = sorted(ab, key=lambda i: i[1])#,reverse=True)
# ab = sorted(ab, key=lambda i: i[0])#,reverse=True)

g = collections.defaultdict(list)
for frm, to in zip(a, b):
    g[frm].append(to)
    g[to].append(frm)
    # heappush(g[frm],to)
    # heappush(g[to],frm)

for i in range(1,n+1):
    g[i].sort()

q = []
visited = [-1 for _ in range(n+1)]
visits = []
# is_edges = [True for _ in range(n+1)]
def dfs(x):
    if visited[x] == 1:
        return 
    visits.append(x)
    visited[x] = 1
    is_edge = True
    for i in g[x]:
        if visited[i] == 1:
            continue
        # is_edges[x] = False
        is_edge = False
        dfs(i)
        visits.append(x)
    # if not is_edge:
        # visits.append(x)

dfs(1)
# print(visits)
for i in visits:
    print(i,end=" ")

