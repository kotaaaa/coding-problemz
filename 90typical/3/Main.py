
#########################
# 幅優先探索
# collections, deque を使う．
#########################

from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

max_distance = 0
i = 1
max_distance_i = 0
for _ in range(2):
    # print("==== ",i," =====")
    visited = [0 for _ in range(n+1)]
    queue = deque()
    queue.append(i)
    visited[i] = 1
    while len(queue) > 0:
        target = queue.pop()
        for j in graph[target]:
            if visited[j] >= 1:
                continue
            queue.append(j)
            visited[j] = visited[target] + 1
            if visited[j] > max_distance:
                max_distance = visited[j]
                max_distance_i = j
        i = max_distance_i
        # print(queue,max_distance,max_distance_i)
print(max_distance)