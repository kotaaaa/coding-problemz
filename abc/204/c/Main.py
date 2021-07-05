import collections
from collections import deque

n,m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
if m == 0:
    print(n)
    exit()
a,b = [list(i) for i in zip(*ab)]

adjacent_dict = collections.defaultdict(list)
for i in range(m):
    adjacent_dict[a[i]].append(b[i])

# print(adjacent_dict)
ans = 0
for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    queue = deque()
    queue.append(i)
    visited[i] = 1
    ans += 1
    while len(queue) > 0:
        target = queue.pop()
        # print("i target",i,target)
        # if visited[target] >= 1:
            # continue
        for j in adjacent_dict[target]:
            if visited[j] >= 1:
                continue
            queue.append(j)
            visited[j] = 1
            ans += 1
    # print(ans)
print(ans)