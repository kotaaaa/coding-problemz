n, q = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n - 1)]
a, b = [list(i) for i in zip(*ab)]
px = [map(int, input().split()) for _ in range(q)]
p, x = [list(i) for i in zip(*px)]


import collections
from collections import deque

adjacent_dict = collections.defaultdict(list)
for i in range(n - 1):
    adjacent_dict[a[i]].append(b[i])
    adjacent_dict[b[i]].append(a[i])

parents_cnt = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(q):
    parents_cnt[p[i]] += x[i]
# print(parents_cnt)
# print(adjacent_dict)

queue = deque()
queue.append(1)
# visited[1] = 1
while len(queue) > 0:
    target = queue.popleft()
    if visited[target] == 1:
        continue
    visited[target] = 1
    for i in adjacent_dict[target]:
        if visited[i] == 1:
            continue
        parents_cnt[i] += parents_cnt[target]
        queue.append(i)
# print(parents_cnt)
for i in range(1, n + 1):
    print(parents_cnt[i], end=" ")
# print(parents_cnt[n-1])