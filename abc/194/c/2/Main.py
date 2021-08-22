n = int(input())
a = list(map(int, input().split()))
times = [0 for i in range(401)]

ans = 0
sum_pow2 = 0 

for i in range(n):
    for aj in range(-200, 201):
        c = times[200+aj]
        x = a[i]-aj
        ans += x*x*c
    # times[200+a[i]] += 1
    times[a[i] + 200] += 1
print(ans)


