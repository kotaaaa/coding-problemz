n,m = map(int,input().split())
py = [map(int, input().split()) for _ in range(m)]
p,y = [list(i) for i in zip(*py)]

import heapq

# queue_list = [heapq.heapify([]) for _ in range(m)]
queue_list = [[] for _ in range(n+1)]
# print(queue_list)
for i in range(m):
    # heapq.heappush(queue_list[p[i]],[y[i],i])
    queue_list[p[i]].append([y[i],i])
# print(queue_list[:10])

city_list = []
for i in range(n+1):
    if len(queue_list[i]) != 0:
        heapq.heapify(queue_list[i])
        city_list.append([i,queue_list[i]])
        # city_list.append([i,queue_list[i]])

# print(city_list)

order_list = []
# while len(city_list) > 0:
for i in city_list:
    # i = city_list.heappop()
    e = 0
    # for e,j in enumerate(i[1]):
    while len(i[1]) > 0:
        j = heapq.heappop(i[1])
        # print("0" * (6-len(str(i[0])))+str(i[0])+"0" * (6-len(str(e+1)))+str(e+1))
        order_list.append([("0" * (6-len(str(i[0])))+str(i[0])+"0" * (6-len(str(e+1)))+str(e+1)),j[1]])
        e += 1
# print(order_list)
sorted_order_list = sorted(order_list, key=lambda i: i[1])
for i in sorted_order_list:
    print(i[0])