from collections import deque
from heapq import heappop, heappush
# import heapq

q = int(input())
qz = [list(map(int,input().split())) for _ in range(q)]

num_dict = []
adds = 0 
tmp_adds = 0
for i in range(q):
    # print("num_dict",i,num_dict)
    if qz[i][0] == 1:
        # if qz[i][1] in num_dict:
        #     num_dict[qz[i][1]] += 1
        # else:
        #     num_dict[qz[i][1]] = 1
        heappush(num_dict, qz[i][1] - adds)
    elif qz[i][0] == 2:
        adds += qz[i][1]
    else:
        # print("aa",heappop(num_dict))
        # print(heappop(num_dict))
        print(heappop(num_dict)+adds)
