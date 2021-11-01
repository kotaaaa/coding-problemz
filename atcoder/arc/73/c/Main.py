n,t = map(int, input().split())
tz = list(map(int, input().split()))

current = tz[0]
times = 0
for i in range(1,n):
    if tz[i] - current < t:
        times += tz[i] - current
        current = tz[i]
    else:
        times += t
        current = tz[i]
print(times+t)

