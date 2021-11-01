from heapq import heappop, heappush, heapify
h,w,n = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

qa = []
qb = []
a_idx = [0 for i in range(n)]
b_idx = [0 for i in range(n)]

for i in range(n):
    heappush(qa,(a[i], i))
    heappush(qb,(b[i], i))
    # qa.append(a[i])
    # qb.append(b[i])
# qa.sort()
# qb.sort()
# print(qa)
# print(qb)

idx = 1
before = -1
for i in range(n):
    target = heappop(qa)
    # print(target)
    a_idx[target[1]] = idx 
    if i == 0:
        before = target[0]
        a_idx[target[1]] = idx 
        continue
    if target[0] == before:
        before = target[0]
        a_idx[target[1]] = idx 
        continue
    before = target[0]
    idx += 1
    a_idx[target[1]] = idx 

idx = 1
before = -1
for i in range(n):
    target = heappop(qb)
    # print(target)
    b_idx[target[1]] = idx 
    if i == 0:
        before = target[0]
        b_idx[target[1]] = idx 
        continue
    if target[0] == before:
        before = target[0]
        b_idx[target[1]] = idx 
        continue
    before = target[0]
    idx += 1
    b_idx[target[1]] = idx 

    # print(heappop(qb))
# print(qb)
for i in range(n):
    print(a_idx[i],b_idx[i])
