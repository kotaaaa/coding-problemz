##############
### マンハッタン距離， 45度回転 ###
##############


n,q= map(int, input().split())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
qz = [int(input()) for _ in range(q)]

p = []
inf = 10**10
min_s = min_t = inf
max_s = max_t = -inf
for i in range(n):
    s = x[i]+y[i]
    t = x[i]-y[i]
    p.append((s, t))
    min_s = min(min_s, s)
    min_t = min(min_t, t)
    max_s = max(max_s, s)
    max_t = max(max_t, t)

for i in range(q):
    s, t = p[qz[i]-1]
    ans = max(s-min_s, t-min_t, max_s-s, max_t-t)
    print(ans)

