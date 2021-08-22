from heapq import heappop, heappush
h,w,n = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

qa = []
qb = []

a_idx = [0 for i in range(n)]
b_idx = [0 for i in range(n)]

for i in range(n):
    # heappush(qa,(a[i], i))
    # heappush(qa,(a[i], i+1))
    # heappush(qb,(b[i], i))
    

print(qa)
print(qb)

idx = 1
before = -1
for i in range(n):
    a_idx[qa[i][1]] = idx
    if i == 0:
        before = qa[i][1]
        continue
    if qa[i][1] != before:
        idx += 1
        before = qa[i][1]

idx = 1
before = -1
for i in range(n):
    b_idx[qb[i][1]] = idx
    if i == 0:
        before = qb[i][1]
        continue
    if qb[i][1] != before:
        idx += 1
        before = qb[i][1]
        

for i in range(n):
    print(a_idx[i],b_idx[i])


    # heappush(qa,(a[i], i+1))
    # heappush(qa,(a[i], i+1))
    # heappush(qb,(b[i], i+1))


# print(qa)
# print(qb)

# sorted_qa = sorted(qa, key=lambda i: i[1])
# sorted_qb = sorted(qb, key=lambda i: i[1])