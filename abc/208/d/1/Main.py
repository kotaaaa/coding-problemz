from heapq import heappop, heappush
import collections

n,m = map(int,input().split())
a = [0 for _ in range(m)]
b = [0 for _ in range(m)]
c = [0 for _ in range(m)]

for i in range(m):
    a[i],b[i],c[i] = map(int,input().split())

ans = 0
inf = 10 ** 9
g = collections.defaultdict(list)
for frm, to, cost in zip(a, b, c):
    g[frm].append([to, cost])
    ans += cost

for k in range(1,n+1):
    # print("k",k)
    for s in range(1,n+1):
        # print("s",s)
        # for t in range(1,n+1):
        # print("s,t,k",s,t,k)
        q = []
        q.append((0, s))
        confirmed = [0] * (n + 1)
        min_cost = [inf] * (n + 1)
        while len(q) > 0:
            target_cost, target_city = heappop(q)
            # print(target_city, target_cost, s,t,k)
            if confirmed[target_city] == 1:
                continue
            if target_city > k and (target_city != s):
                continue
            # print("aaaaa")
            confirmed[target_city] = 1
            min_cost[target_city] = target_cost
            for road, cost in g[target_city]:
                # print("r",road,cost)
                if confirmed[road] == 1:
                    continue
                if target_city > k and (target_city != s):
                    continue
                # print("target_cost + cost", target_cost, cost)
                min_cost[road] = min(target_cost + cost, min_cost[road])
                heappush(q, (min_cost[road], road))
        # print(min_cost[1:])
        for t in range(n):
            if s == t:
                continue
            if min_cost[t] == inf:
                continue
            ans += min_cost[t]
        # print("ans>>", min_cost[t],ans)


print(ans)