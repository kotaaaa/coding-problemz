n = int(input())
at = [map(int, input().split()) for _ in range(n)]
a, t = [list(i) for i in zip(*at)]
q = int(input())
x = list(map(int, input().split()))

INF = 1 << 60
l = -INF
r = INF
s = 0
for i in range(n):
    if t[i] == 1:
        s += a[i]
        l += a[i]
        r += a[i]
    elif t[i] == 2:
        l = max(l, a[i])
        r = max(r, a[i])
    else:
        l = min(l, a[i])
        r = min(r, a[i])

for i in x:
    # ans = 0
    res = i + s
    if res < l:
        res = l
    elif res > r: 
        res = r
    print(res)

