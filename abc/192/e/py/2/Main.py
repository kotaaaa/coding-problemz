import math
import sys 
import collections
from heapq import heappop, heappush

n,m,x,y = map(int,input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 隣接リスト
adjacent_dict = collections.defaultdict(list)
for frm, to, distance, k in edges:
    adjacent_dict[frm].append([to, distance, k])
    adjacent_dict[to].append([frm, distance, k])

queue = []
distances = collections.defaultdict(lambda: sys.maxsize)
queue.append((0,x)) # 時間, 街, 時刻表，スタート時点
while len(queue) > 0:

    target_cost, target_node = heappop(queue)
    print("target_cost, target_node ", target_cost, target_node)
    print("distances1 ",distances)
    if distances[target_node] != sys.maxsize:
        continue

    distances[target_node] = target_cost

    for road, distance, interval in adjacent_dict[target_node]:
        print("road, distance, interval ", road, distance, interval)
        # print("distances2 ",distances)
        if distances[road] != sys.maxsize:
            print("no max")
            continue
        wait_time = (interval - (distances[target_node] % interval)) % interval
        next_candidate_time = (distances[target_node] # 確定ノードまでの時間 
        + distance  # 次の駅までにかかる時間
        + wait_time)  # 電車出発までの待ち時間
        heappush(queue, (next_candidate_time, road))
        # print("distances3 ",distances)
if (distances[y] == sys.maxsize):
    print(-1)
    sys.exit()
print(distances[y])