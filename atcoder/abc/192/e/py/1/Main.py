## 以下ACしている．

import math
import sys 
import collections
from heapq import heappop, heappush

n,m,x,y = map(int,input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

# 隣接リスト
adjacent_dict = collections.defaultdict(list)
# i = 0
for frm, to, distance, k in edges:
    adjacent_dict[frm].append([to, distance, k])
    adjacent_dict[to].append([frm, distance, k])

queue = []
confirmed = [0 for i in range(n+1)]
distances = collections.defaultdict(lambda: sys.maxsize)
queue.append((0,x)) # 時間, 街, 時刻表，スタート時点
distances[x] = 0
while len(queue) > 0:
    target_cost, target_node = heappop(queue)
    if confirmed[target_node] == 1:
        continue
    # print("target_cost, target_node ", target_cost, target_node)
    confirmed[target_node] = 1
    for road, distance, interval in adjacent_dict[target_node]:
        # print("road, distance, interval ", road, distance, interval)
        if confirmed[road] == 1:
            continue
        # 電車出発までの待ち時間
        wait_time = 0
        if (distances[target_node] % interval != 0):
            wait_time = interval - (distances[target_node] % interval)
        next_candidate_time = (distances[target_node] # 確定ノードまでの時間 
        + distance  # 次の駅までにかかる時間
        + wait_time)  # 電車出発までの待ち時間
        # print("next_candidate_time, distances[target_node], distance, wait_time ",next_candidate_time, distances[target_node], distance, wait_time)
        if (next_candidate_time < distances[road]):
            distances[road] = next_candidate_time
            heappush(queue, (distances[road], road))
if (distances[y] == sys.maxsize):
    print(-1)
    sys.exit()
print(distances[y])