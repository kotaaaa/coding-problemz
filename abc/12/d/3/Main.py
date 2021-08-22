import math
import sys 
import collections
from heapq import heappop, heappush

n,m = map(int,input().split())

A = [0] * m
B = [0] * m
T = [0] * m

cost = [[0 for i in range(n+1)] for j in range(n+1)]
path = [[] for i in range(n+1)]

for i in range(m):
    #上から順番に代入していく
    A[i], B[i], T[i] = map(int, input().split())
    path[A[i]].append(B[i])
    path[B[i]].append(A[i])
    cost[A[i]][B[i]] = T[i]
    cost[B[i]][A[i]] = T[i]

# ans_dict = [0 for i in range(n+1)]
ans_dict = collections.defaultdict(lambda: sys.maxsize)
for i in range(1,n+1):

    queue = []
    confirmed = [0 for i in range(n+1)]
    # distances = [10000 for i in range(n+1)]
    distances = collections.defaultdict(lambda: sys.maxsize)
    queue.append((0,i))
    distances[i] = 0
    while len(queue) > 0:
        target_cost, target_node = heappop(queue)
        confirmed[target_node] = 1
        for road in path[target_node]:
            if confirmed[road] == 1:
                continue
            if (cost[target_node][road] + distances[target_node] < distances[road]):
                distances[road] = min(cost[target_node][road] + distances[target_node], distances[road])
                heappush(queue, (distances[road], road))
        # ans_dict[i] = max (distances[target_node], ans_dict[i])
        ans_dict[i] = max(distances.values())
    
# print(min(ans_dict[1:]))
print(min(ans_dict.values()))


###  以上はできる．
###  以下はできないなぞ．


# import collections
# import sys
# import math
# import heapq  # import heappop, heappush

# n,m = map(int,input().split())

# A = [0] * m
# B = [0] * m
# T = [0] * m

# # cost = [[0 for i in range(n+1)] for j in range(n+1)]
# # path = [[] for i in range(n+1)]

# for i in range(m):
# #     #上から順番に代入していく
#     A[i], B[i], T[i] = map(int, input().split())
# #     path[A[i]].append(B[i])
# #     path[B[i]].append(A[i])
# #     cost[A[i]][B[i]] = T[i]
# #     cost[B[i]][A[i]] = T[i]
# adjacent_dict = collections.defaultdict(list)
# for i in range(m):
#     adjacent_dict[A[i]].append([B[i], T[i]])
#     adjacent_dict[B[i]].append([A[i], T[i]])


# # print(path)

# # queue = []
# # confirmed = [0 for i in range(n+1)]
# # distances = [10000 for i in range(n+1)]
# # min_distance = 10000;
# # each_max_distance = 0;

# ans_dict = collections.defaultdict(lambda: sys.maxsize)


# for i in range(1,n+1):

#     distances = collections.defaultdict(lambda: sys.maxsize)
#     queue = []
#     # confirmed = [0 for i in range(n+1)]
#     confirmed = collections.defaultdict(lambda: 0);
#     # distances = [10000 for i in range(n+1)]

#     # print("\n\n i+1 ",(i+1))
#     # queue.append((0,i))
#     heapq.heappush(queue, (0,i))
#     distances[i] = 0
#     while len(queue) > 0:
#         # print("queue ",queue)
#         target_cost, target_node = heapq.heappop(queue)
#         # print("target[0] ",target[0])
#         # print("target_cost ",target_cost, " target_node ",target_node, " path[target_node] ",path[target_node])
        
#         confirmed[target_node] = 1
#         # print("path[target_node] ",path[target_node])
#         # print("confirmed ",confirmed)
#         # print("distances ",distances)
#         # print("target_node ",target_node)
#         for road, cost in adjacent_dict[target_node]:
#             # print("road ",road," cost[target_node][road] ",cost[target_node][road])
#             if confirmed[road] == 1:
#                 continue
#             # print("cost[target_node][road]  ",cost[target_node][road]," distances[target_node] ",distances[target_node]," distances[road] ",distances[road])
#             # distances[road] = min(cost[target_node][road] + distances[target_node], distances[road])
#             distances[road] = min(cost + distances[target_node], distances[road])
#             heapq.heappush(queue, (distances[road], road))
#             # print(road)
#         # each_max_distance = max (distances[road], each_max_distance)
#     # print("last node distance ",distances[target_node])

#     # min_distance = min (min_distance, distances[target_node])
#     ans_dict[i] = max(distances.values())

# print(min(ans_dict.values()))