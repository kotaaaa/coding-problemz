from heapq import heapify, heappop, heappush
n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
# heapify(t)
# for i in range(n):
    # [t[i],i]
queue = [[t[i],i] for i in range(n)]
heapify(queue)

cnt = 0
confirmed = [-1 for _ in range(n)]
times = [-1 for _ in range(n)]
while cnt < n:
    target = heappop(queue)
    if confirmed[target[1]] == 1:
        continue
    times[target[1]] = target[0]
    heappush(queue,[target[0] + s[target[1]], (target[1]+1) % n])
    cnt += 1
    confirmed[target[1]] = 1
for i in range(n):
    print(times[i])



