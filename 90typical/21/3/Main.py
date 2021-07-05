############
## SCC 強連結成分分解
############
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(M)]
# 有向グラフの典型入力を双方向で適用
adj, adj_inv = defaultdict(set), defaultdict(set)
for a, b in S:
    adj[a - 1].add(b - 1)
    adj_inv[b - 1].add(a - 1)
seen = [False] * N
backward_list = []


def dfs1(pos):
    seen[pos] = True
    for next_ in adj[pos]:
        if not seen[next_]:
            dfs1(next_)
    backward_list.append(pos)  # 帰りがけ
    return


for n in range(N):
    if not seen[n]:
        dfs1(n)

seen = [False] * N
groups = defaultdict(set)


def dfs2(pos, label):
    seen[pos] = True
    groups[label].add(pos)  # 行きがけ
    for next_ in adj_inv[pos]:  # 逆向きを探索
        if not seen[next_]:
            dfs2(next_, label)
    return


ans = 0
label = 0
for n in reversed(backward_list):  # 帰りがけの逆順
    if not seen[n]:
        dfs2(n, label)
        label += 1
for k, v in groups.items():
    num = len(v)
    ans += num * (num - 1) // 2
print(ans)