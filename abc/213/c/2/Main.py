from heapq import heappop, heappush, heapify
h,w,n = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

qa = []
# heapify(qa)
qb = []
# heapify(qb)
a_idx = [0 for i in range(n)]
b_idx = [0 for i in range(n)]
# print(b)
for i in range(n):
    heappush(qa,(a[i], i))
    # print((b[i], i+1),qb)
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
exit()

qa2 = [-1 for _ in range(n)]
qb2 = [-1 for _ in range(n)]

qa2[qa[0][1]] = qa[0][0]
qb2[qb[0][1]] = qb[0][0]
# qb2 = [qb[0]]

idx = 1
for i in range(1,n):
    if qa[i] != qa[i-1]:
        idx += 1
    qa2.append(idx)

idx = 1
for i in range(1,n):
    if qb[i] != qb[i-1]:
        idx += 1
    qb2.append(idx)

for i in range(n): 
    print(qa2[i],qb2[i])