############
## 深さ優先探索 / dfs >> これは結局間違い
############
import collections
from collections import deque
import copy

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
if m != 0:
    xy = [list(map(int, input().split())) for _ in range(m)]
    x, y = [list(i) for i in zip(*xy)]

g = [[i+1 for i in range(n)] for _ in range(n)]

if m != 0:
    for frm, to in zip(x, y):
        g[frm-1].remove(to)
        g[to-1].remove(frm)

nodes = []
orders = []
def dfs (node):
    visited[node] = True
    nodes.append(node)  # 行きがけ
    if len(nodes) == n:
        orders.append(copy.deepcopy(nodes))
        visited[node] = False
        nodes.pop()
        return 
    for next_ in g[node-1]:
        if not visited[next_]:
            dfs(next_)
    visited[node] = False
    nodes.pop()  # 帰りがけ
    return

visited = [0 for _ in range(n+1)]
for i in range(1,n+1):
    visited = [False for _ in range(n+1)]
    nodes = []
    dfs(i)
ans = 10**9
for order in orders:
    time = 0
    for i in range(n):
        time += a[order[i]-1][i]
    ans = min(time,ans)

if ans == 10**9:
    print(-1)
    exit()
print(ans)
        