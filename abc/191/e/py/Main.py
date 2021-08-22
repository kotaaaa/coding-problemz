import math
import sys 
import collections
from heapq import heappop, heappush

n,m = map(int,input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

# 隣接リスト
adjacent_dict = collections.defaultdict(list)
for frm, to, distance in edges:
    adjacent_dict[frm].append([to, distance])

# print(adjacent_dict)
ans_dict = collections.defaultdict(list)

for i in range(1,n+1):

    ## 自分への道があるとき
    # print(i,adjacent_dict[i],adjacent_dict[i][0], (adjacent_dict[i][0] == i))
    # if adjacent_dict[i][0] == i:
        # ans_dict[i] = adjacent_dict[i][1]
        # continue

    ## ダイクストラ
    queue = []
    confirmed = [0 for i in range(n+1)]
    distances = collections.defaultdict(lambda: sys.maxsize)
    queue.append((0,i)) # 距離, 街
    distances[i] = 0
    distance_i = sys.maxsize
    while len(queue) > 0:
        target_cost, target_node = heappop(queue)
        if confirmed[target_node] == 1:
            continue
        # print("target_cost, target_node ", target_cost, target_node)
        confirmed[target_node] = 1
        for road, distance in adjacent_dict[target_node]:
            # print("road, distance ", road, distance,)
            if confirmed[road] == 1 and road != i:
                continue
            
            next_candidate_time = distance + distances[target_node]
            # print("next_candidate_time, distances[target_node], distance ",next_candidate_time, distances[target_node], distance)
            if road == i: ## 次の道が最終ゴールのとき
                if next_candidate_time < distance_i:
                    distance_i = next_candidate_time
                    # heappush(queue, (distance_i, road))                 
            else: ## 次の道が最終ゴール以外のとき
                if next_candidate_time < distances[road]:
                    distances[road] = next_candidate_time
                    heappush(queue, (distances[road], road)) 
    if distance_i == sys.maxsize:
        ans_dict[i] = -1
    else:
        ans_dict[i] = distance_i
# print(ans_dict)
for key in ans_dict:
    print(ans_dict[key])


