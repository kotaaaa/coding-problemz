n = int(input())
a = list(map(int, input().split()))
times = [0 for i in range(401)]

ans = 0
sum_pow2 = 0

for i in range(n):
    times[a[i]+200] += 1

for i in range(-200, 201):
    for j in range(i+1, 201):
        cai = times[200+i]
        caj = times[200+j]
        ans += cai*caj*pow(i-j, 2)
print(ans)



