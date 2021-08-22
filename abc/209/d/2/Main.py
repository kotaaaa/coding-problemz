from heapq import heappop, heappush
import collections

n,m = map(int,input().split())
a = [0 for _ in range(m)]
b = [0 for _ in range(m)]
c = [0 for _ in range(m)]

for i in range(m):
    a[i],b[i],c[i] = map(int,input().split())

ans = 0
inf = 10 ** 9
# g = collections.defaultdict(list)
g = [[inf for _ in range(n+1)] for _ in range(n+1)]
for frm, to, cost in zip(a, b, c):
    g[frm][to] = cost

for i in range(1,n+1):
    g[i][i] = 0

for k in range(1,n+1):
    next = [[inf for _ in range(n+1)] for _ in range(n+1)]
    for s in range(1,n+1):
        for t in range(1,n+1):
            next[s][t] = min(g[s][t], g[s][k] + g[k][t])
            if next[s][t] < inf:
                ans += next[s][t]
    g = next

print(ans)
