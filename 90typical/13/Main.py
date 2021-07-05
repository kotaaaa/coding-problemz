## ダイクストラ．Dijkstra
from heapq import heappop, heappush
import collections

n, m = map(int, input().split())
a = [0] * m
b = [0] * m
c = [0] * m

for i in range(m):
    a[i], b[i], c[i] = map(int, input().split())

g = collections.defaultdict(list)
for frm, to, distance in zip(a, b, c):
    g[frm].append([to, distance])
    g[to].append([frm, distance])

q = []
q.append((0, 1))
confirmed = [0] * (n + 1)
min_cost = [10 ** 9] * (n + 1)
while len(q) > 0:
    target_cost, target_city = heappop(q)
    if confirmed[target_city] == 1:
        continue
    confirmed[target_city] = 1
    min_cost[target_city] = target_cost
    for road, cost in g[target_city]:
        if confirmed[road] == 1:
            continue
        # print("target_cost + cost", target_cost, cost)
        min_cost[road] = min(target_cost + cost, min_cost[road])
        heappush(q, (min_cost[road], road))
# print(min_cost)
q = []
q.append((0, n))
confirmed = [0] * (n + 1)
min_cost_n = [10 ** 9] * (n + 1)
while len(q) > 0:
    target_cost, target_city = heappop(q)
    # print("target_city, target_cost", target_city, target_cost)
    if confirmed[target_city] == 1:
        continue
    confirmed[target_city] = 1
    min_cost_n[target_city] = target_cost
    for road, cost in g[target_city]:
        if confirmed[road] == 1:
            continue
        # print("target_cost + cost",target_cost, cost)
        min_cost_n[road] = min(target_cost + cost, min_cost_n[road])
        heappush(q, (min_cost_n[road], road))

# print(min_cost_n)
# print(min_cost + min_cost_n)
for i in range(1, n + 1):
    print(min_cost[i] + min_cost_n[i])

