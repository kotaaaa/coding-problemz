############
## dfs, 木dp,
############

import collections, sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
ab = [map(int, input().split()) for _ in range(n - 1)]
a, b = [list(i) for i in zip(*ab)]

g = collections.defaultdict(list)
for frm, to in zip(a, b):
    g[frm].append(to)
    g[to].append(frm)

def dfs(u: int, par: int) -> None:
    for i in g[u]:
        if i == par:
            continue
        dfs(i, u)
        size[u] += size[i]


size = [1] * (n + 1)
dfs(1, 0)


ans = 0
for i in range(1, n + 1):
    ans += size[i] * (n - size[i])

print(size)

print(ans)