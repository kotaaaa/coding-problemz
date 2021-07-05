## ダイクストラ．Dijkstra
from heapq import heappop, heappush

h, w = map(int, input().split())
c = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    c[i] = list(map(int, input().split()))

a = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    a[i] = list(map(int, input().split()))

magics = [0 for _ in range(10)]

for i in range(10):
    confirmed = [0 for _ in range(10)]
    queue = []
    queue.append((0,i))
    distances = [2*10**5+1 if x != i else 0 for x in range(10)]
    confirmed = [0 for _ in range(10)]

    while len(queue) > 0:
        target_cost, target_node = heappop(queue)
        if target_node == 1:
            break
        if confirmed[target_node] == 1: # or target_node == i:
            continue
        confirmed[target_node] = 1
        for road, distance in enumerate(c[target_node]):
            if confirmed[road] == 1 or road == i:
                continue
            candidate_distance = distance + distances[target_node]
            distances[road] = min(candidate_distance, distances[road])
            heappush(queue, (distances[road], road))
    magics[i] = distances[1]




ans = 0 
for i in range(h):
    for j in range(w):
        if a[i][j] == -1:
            continue
        ans += magics[a[i][j]]
print(ans)